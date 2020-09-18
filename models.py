from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_path = Column(String, unique=True, index=True)
    full_url = Column(String, unique=True)
    clicks = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
