from sqlalchemy.orm import Session

import models, schemas


def create_url(short_url: str, origin_url: str, db: Session):
    db_url = models.Url(short_url=short_url, origin_url=origin_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_origin_url(db: Session, short_url: str):
    return db.query(models.Url.origin_url).filter(models.Url.short_url == short_url).first()

def get_short_url(db: Session, origin_url: str):
    return db.query(models.Url.short_url).filter(models.Url.origin_url == origin_url).first()