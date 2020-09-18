from sqlalchemy.orm import Session

import models, schemas


def create_url(short_path: str, full_url: str, db: Session):
    db_url = models.Url(short_path=short_path, full_url=full_url, clicks=1)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_full_url(db: Session, short_path: str):
    return db.query(models.Url.full_url, models.Url.clicks).filter(models.Url.short_path == short_path).first()

def get_short_path(db: Session, full_url: str):
    return db.query(models.Url.short_path, models.Url.clicks).filter(models.Url.full_url == full_url).first()

def update_click(db: Session, full_url: str):
    db.query(models.Url.clicks).filter(models.Url.full_url == full_url).update({'clicks' : models.Url.clicks + 1}, synchronize_session=False)
    db.commit()
    row = db.query(models.Url.clicks).filter(models.Url.full_url == full_url).first()
    return row.clicks