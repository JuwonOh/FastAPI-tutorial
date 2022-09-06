from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostCreate(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int = 0


class PostDB(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int = 0
