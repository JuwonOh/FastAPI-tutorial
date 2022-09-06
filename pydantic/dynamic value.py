from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


def list_factory():
    return ["a", "b", "c"]


class Model(BaseModel):
    l: List[str] = Field(defualt_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: List[str] = Field(default_factory=list)
