from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine
from app.routers import general

from dotenv import load_dotenv

from app import models

# DATA BASE init
models.Base.metadata.create_all(bind=engine)


load_dotenv()

app = FastAPI()

app.mount('/static', StaticFiles(directory='./app/static'), name='static')

app.include_router(general.router)

