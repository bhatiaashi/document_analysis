from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from auth import require_role
import shutil, os

router = APIRouter()
ALLOWED_EXTENSIONS = {"pptx", "docx", "xlsx"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), role=Depends(require_role("ops"))):
    ext = file.filename.split(".")[-1]
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=422, detail="Invalid file type")

    os.makedirs("storage", exist_ok=True)
    with open(f"storage/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File uploaded successfully", "filename": file.filename}