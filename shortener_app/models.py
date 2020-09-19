from datetime import datetime
from sqlalchemy import  Column, Integer, String, DateTime

from . database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_path = Column(String, unique=True, index=True)
    full_url = Column(String, unique=True, index=True)
    clicks = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
