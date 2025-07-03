from fastapi import FastAPI
from ops_routes import router as ops_router
from client_routes import router as client_router

app = FastAPI()
app.include_router(ops_router, prefix="/ops")
app.include_router(client_router, prefix="/client")