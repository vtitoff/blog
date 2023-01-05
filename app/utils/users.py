import typing as tp
import asyncio
from app.context import AppContext
from app import storage
from app import dto
from app import models


async def fetchall(context: AppContext) -> tp.List[models.User]:
    db_users = await storage.get_all_users(context)
    return db_users
