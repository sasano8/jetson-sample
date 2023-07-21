import asyncio
from typing import List
from fastapi import FastAPI

from .injest import watch_and_ingest

app = FastAPI()
bg_tasks: List[asyncio.Task] = []


@app.on_event("startup")
async def startup():
    global bg_tasks

    for coro in get_backgrounds():
        task = asyncio.create_task(coro)
        bg_tasks.append(task)
    
@app.on_event("shutdown")
async def shutdown():
    global bg_tasks

    for task in bg_tasks:
        task.cancel()


def get_backgrounds():
    yield watch_and_ingest(interval=5, dispatcher=print)

