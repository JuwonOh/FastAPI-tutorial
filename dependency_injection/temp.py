from fastapi import FastAPI, Header, Depends, Query
from typing import Tuple

app = FastAPI()


@app.get("/")
async def header(user_agent: str = Header("....")):
    return {"user_agent": user_agent}


async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    return (skip, limit)


@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


# query function을 사용해서 validation을 가능하게 하기
async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


@app.get("/things")
async def list_thing(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


# class로 구현하는 것도 가능.
class pagination:
    def __init__(self, maximum_limit: int = 100):
        self.maximum_limit = maximum_limit

    async def __call__(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0)
    ) -> Tuple[int, int]:
        capped_limit = min(self.maximum_limit, limit)
        return (skip, capped_limit)
