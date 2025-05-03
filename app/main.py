from fastapi import FastAPI
from app.api.routes import api_router

app = FastAPI()

# Include all routes from api/routes.py
app.include_router(api_router)
