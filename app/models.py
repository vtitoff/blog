from __future__ import annotations
import dataclasses
import json
import asyncpg
from app import dto
from typing import Optional, List


@dataclasses.dataclass(frozen=True)
class Service:
    name: str
    cost: float
    currency: str

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Optional[List[Service]]:
        services = []
        for service in json.loads(row):
            services.append(
                cls(
                    name=service["name"],
                    cost=service["cost"],
                    currency=service["currency"],
                )
            )
        return services


@dataclasses.dataclass(frozen=True)
class User:
    login: str
    first_name: str
    last_name: str
    user_info: str
    services: list[Service]

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> User:
        return cls(
            login=row["login"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            user_info=row["user_info"],
            services=Service.from_db(row["services"]),
        )
