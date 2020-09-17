from pydantic import BaseModel


class Url(BaseModel):
    short_url : str
    origin_url : str
    class Config:
        orm_mode = True

class UrlCreate(BaseModel):
    url : str
