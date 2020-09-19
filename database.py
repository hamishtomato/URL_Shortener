from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://wayrdthwudihxs:928c480a6b72ffae76da47d13bcab7983c341a6354de1f7af18113353e8e28dc@ec2-52-200-134-180.compute-1.amazonaws.com:5432/d4rdojto7v9b8a"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()