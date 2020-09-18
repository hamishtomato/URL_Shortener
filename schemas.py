from pydantic import BaseModel, HttpUrl


# class Url(BaseModel):
#     short_url : HttpUrl
#     origin_url : HttpUrl
#     class Config:
#         orm_mode = True

class UrlCreate(BaseModel):
    url : HttpUrl