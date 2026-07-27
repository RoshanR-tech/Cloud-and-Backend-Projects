from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routes import router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Face Mask Detection API",
    description="AI-powered Face Mask Detection using FastAPI",
    version="1.0.0"
)

app.mount("/uploads", StaticFiles(directory=BASE_DIR / "uploads"), name="uploads")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

app.include_router(router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )