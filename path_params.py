from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


@app.get("/users/{type}/{id}")
async def get_user(type: str, id: int):
    return {"type": type, "id": id}
