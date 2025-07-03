from fastapi import Header, HTTPException

def require_role(expected: str):
    def checker(role: str = Header(...)):
        if role != expected:
            raise HTTPException(status_code=403, detail="Unauthorized")
    return checker