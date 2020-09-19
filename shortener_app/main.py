import hashlib
from urllib.parse import urlparse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import RedirectResponse
from functools import lru_cache

from . import crud, models, schemas
from . database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def encode_url(url):
    md5 = hashlib.md5()
    md5.update(url.encode("utf8"))
    return md5.hexdigest()[:10]

@app.post("/urls/register")
async def register_url(request: Request, body: schemas.UrlCreate, db: Session = Depends(get_db)):
    url_parse = urlparse(str(request.url))
    row = crud.get_short_path(db, full_url=body.url)
    if row:
        clicks = crud.update_click(full_url=body.url, db=db)
        short_url = '{}://{}/{}'.format(url_parse.scheme , url_parse.netloc , row.short_path)
        return {"short_url": short_url, "clicks": clicks}
    short_url_path = encode_url(body.url)
    row = crud.create_url(short_path=short_url_path, full_url=body.url, db=db)
    short_url = '{}://{}/{}'.format(url_parse.scheme , url_parse.netloc , short_url_path)
    return {"short_url": short_url, "clicks": row.clicks}

@app.get("/{short_path}")
def read_users(short_path, db: Session = Depends(get_db)):
    urls = crud.get_full_url(db, short_path=short_path)
    crud.update_click(short_path=short_path, db=db)
    response = RedirectResponse(url=urls.full_url)

    return response