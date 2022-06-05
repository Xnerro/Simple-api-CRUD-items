from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.route import router as route
from src.models.db import Base, engine

templates = Jinja2Templates(directory='public')

app = FastAPI(title='Api Barang')