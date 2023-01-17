import typing as tp
import asyncio
from app.context import AppContext
from app import storage, models, dto


async def get_services_by_login(ctx: AppContext, login: str) -> tp.List[models.Service]:
    db_services = await storage.get_services_by_login(ctx, login)
    return db_services


async def fetchone(ctx: AppContext, id: str) -> models.Service:
    service = await storage.get_service(ctx, id)
    return service


async def create_service(ctx: AppContext, **kwargs) -> models.Service:
    service_is_created = await storage.create_service(ctx, **kwargs)
    if service_is_created:
        service = await storage.get_service(ctx, kwargs["id"])
        return service


async def update_service(ctx: AppContext, **kwargs) -> models.Service:
    service = await storage.update_service(ctx, kwargs["id"])
    if service:
        for field in kwargs:
            if field == "id":
                pass
            await storage.update_service_field(ctx, kwargs["id"], field, kwargs[field])
        service = await storage.get_service(ctx, kwargs["id"])
        return service


async def delete_service(ctx: AppContext, id: str) -> str:
    service_is_deleted = await storage.delete_service(ctx, id)
    if service_is_deleted:
        return "service is deleted"
