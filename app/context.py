from __future__ import annotations
import typing as tp
import pathlib
import asyncpg
from app.utils import secrets


class AppContext:
    def __init__(self, *, secrets_dir: pathlib.Path):
        self.secrets = secrets.SecretsReader(secrets_dir)
        self.db: tp.Optional[asyncpg.Pool] = None

    async def on_startup(self, app=None):
        self.db = await asyncpg.create_pool(self.secrets.get("db"))

    async def on_shutdown(self, app=None):
        if self.db:
            await self.db.close()
