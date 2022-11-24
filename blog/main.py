from fastapi import FastAPI
from .database import engine
from .routers import blog, user
from . import models

# from passlib.context import CryptContext


app = FastAPI()
# create all the models into DB
# (table or migrate all tables  in our   database table)
models.Base.metadata.create_all(engine)

# later we will have user.router so we should define separately
app.include_router(blog.router)
app.include_router(user.router)
