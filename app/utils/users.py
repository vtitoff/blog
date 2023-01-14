import typing as tp
import asyncio
from app.context import AppContext
from app import storage, models, dto


async def fetchall(ctx: AppContext) -> tp.List[models.User]:
    db_users = await storage.get_all_users(ctx)
    return db_users


async def fetchone(ctx: AppContext, login: str) -> models.User:
    user = await storage.get_user(ctx, login)
    return user


async def create_user(ctx: AppContext, **kwargs) -> models.User:
    user_is_created = await storage.create_user(ctx, **kwargs)
    if user_is_created:
        user = await storage.get_user(ctx, kwargs["login"])
        return user


async def update_user(ctx: AppContext, **kwargs) -> models.User:
    user = await storage.get_user(ctx, kwargs["login"])
    if user:
        for field in kwargs:
            if field == "login":
                pass
            await storage.update_users_field(ctx, kwargs["login"], field, kwargs[field])
        user = await storage.get_user(ctx, kwargs["login"])
        return user


async def delete_user(ctx: AppContext, login: str) -> models.User:
    user_is_deleted = await storage.delete_user(ctx, login)
    if user_is_deleted:
        return 'user is deleted'
