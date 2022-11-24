# a for pydantic model called  schema
from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


# To show name, email  & Password
class User(BaseModel):
    name: str
    email: str
    password: str


# To just show name & email
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    # creator: ShowUser

    class Config:
        orm_mode = True
