import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import auth, views
from app.core.config import settings
import os

app = FastAPI()

# Mount Static Files (Model, CSS, JS...)
app.mount("/models", StaticFiles(directory=settings.MODEL_DIR), name="models")
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
# Include Routers (Kết nối các module lại)
app.include_router(views.router)       # Router HTML
app.include_router(auth.router)        # Router API

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)