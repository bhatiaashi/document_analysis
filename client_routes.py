from fastapi import APIRouter, HTTPException, Depends
from auth import require_role
from utils import encrypt_file_id, decrypt_token
import os

router = APIRouter()


@router.post("/signup")
def signup():
    token = encrypt_file_id("example.docx")
    return {"download-link": f"/client/secure-download/{token}"}


@router.get("/secure-download/{token}")
def download_file(token: str, role=Depends(require_role("client"))):
    try:
        filename = decrypt_token(token)
    except:
        raise HTTPException(status_code=403, detail="Invalid token")

    if not os.path.exists(f"storage/{filename}"):
        raise HTTPException(status_code=404, detail="File not found")

    return {"message": "success", "file": filename}