import re
import hashlib
import base62
from urllib.parse import urlparse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import RedirectResponse

import crud, models, schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

def short(url):
    hash = hashlib.md5()
    hash.update(url.encode("utf8"))
    return base62.encodebytes(hash.digest()[-6:])

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/urls/register")
async def register_url(request: Request, body: schemas.UrlCreate, db: Session = Depends(get_db)):
    if not re.match(r'^https?:/{2}\w.+$', body.url):
        raise HTTPException(status_code=400, detail="URL is invalid")

    row = crud.get_short_url(db, origin_url=body.url)
    if row:
        return row.short_url

    short_url_path = short(body.url)
    url_parse = urlparse(str(request.url))
    crud.create_url(short_url=short_url_path, origin_url=body.url, db=db)
    short_url = '{}://{}/{}'.format(url_parse.scheme , url_parse.netloc , short_url_path)
    return short_url

@app.get("/{short_url}")
def read_users(short_url, db: Session = Depends(get_db)):
    urls = crud.get_origin_url(db, short_url=short_url)
    response = RedirectResponse(url=urls.origin_url)
    return response