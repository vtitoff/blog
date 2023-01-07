import typing as tp
import asyncio
from app.context import AppContext
from app import storage, models, dto


async def fetchall(context: AppContext) -> tp.List[models.User]:
    db_users = await storage.get_all_users(context)
    return db_users


async def create_user(context: AppContext, **kwargs) -> models.User:
    user = await storage.create_user(context, **kwargs)
    return user
