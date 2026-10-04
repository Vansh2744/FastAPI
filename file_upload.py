from fastapi import FastAPI, UploadFile,File
from fastapi.staticfiles import StaticFiles
import shutil

app = FastAPI()

app.mount("/files",StaticFiles(directory="uploads"), name="files")

@app.post('/uploads')
async def upload_file(file:UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename,
        "filepath":f"http:127.0.0.1:8000/files/{file.filename}"
    }