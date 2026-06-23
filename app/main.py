from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DB_URL = os.getenv("DATABASE_URL", "postgresql://appuser:apppass@postgres-service:5432/appdb")

@app.get("/")
def root():
    return {"status": "ok", "service": "backend"}

@app.get("/health")
def health():
    try:
        engine = create_engine(DB_URL)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "healthy", "db": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "db": str(e)}
