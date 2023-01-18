import typing as tp
import asyncio
from app.context import AppContext
from app import storage, models, dto
from app import constants
from app.utils import services as service_utils


async def fetchall(
    ctx: AppContext, page, page_limit
) -> tp.Tuple[tp.List[models.User], int]:
    count = await storage.count_all(ctx, constants.USERS_TABLE)
    db_users = await storage.get_all_users(ctx, page, page_limit)
    return db_users, count


async def fetchone(ctx: AppContext, login: str) -> models.User:
    user = await storage.get_user(ctx, login)
    user_services = await service_utils.get_services_by_login(ctx, login)
    return user, user_services


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
        return "user is deleted"
