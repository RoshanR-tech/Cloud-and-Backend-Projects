from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import os

from app.model import predict_image

router = APIRouter()

templates = Jinja2Templates(directory="templates")

print("Current Working Directory:", os.getcwd())
print("Templates Folder Exists:", os.path.exists("templates"))
print("Template File Exists:", os.path.exists("templates/index.html"))

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "image": None,
            "predictions": None,
        },
    )


@router.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    image = Image.open(file_path)

    predictions = predict_image(image)

    print(predictions)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "image": f"/uploads/{file.filename}",
            "predictions": predictions,
        },
    )