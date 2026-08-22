from fastapi import FastAPI
from app.routers import tasks, users
from app.database import engine, Base

app = FastAPI(
    title="Telegram Task Manager",
    description="API для управления задачами через Telegram бота",
    version="1.0.0"
)

app.include_router(tasks.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Telegram Task Manager API работает!"}