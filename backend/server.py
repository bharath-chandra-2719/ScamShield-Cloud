
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lib.db import init_db
from routers.analyze import router as analyze_router
from routers.history import router as history_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("ScamShield database initialized successfully.")
    yield


app = FastAPI(
    title="ScamShield API",
    description="ScamShield - Phishing and Fraudulent Message Detection",
    version="1.0.0",
    lifespan=lifespan
)


allowed_origins = os.getenv("FRONTEND_URL", "*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origin.strip()
        for origin in allowed_origins.split(",")
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(
    analyze_router,
    prefix="/api",
    tags=["Analysis"]
)

app.include_router(
    history_router,
    prefix="/api",
    tags=["History"]
)


@app.get("/")
def root():
    return {
        "name": "ScamShield API",
        "status": "online",
        "database": "cloud-ready"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
