# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import Base, engine
from app.routers import contacts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown logic (if any)

app = FastAPI(lifespan=lifespan)
app.include_router(contacts.router)
