from __future__ import annotations
import dataclasses
import json
import asyncpg
from typing import Optional, List


@dataclasses.dataclass(frozen=True)
class Service:
    id: str
    title: str
    description: str
    cost: float
    currency: str
    user_login: str

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Service:
        return cls(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            cost=row["cost"],
            currency=row["currency"],
            user_login=row["user_login"],
        )

    @classmethod
    def from_request(cls, service: dict) -> Optional[Service]:
        return cls(
            id=service["id"],
            title=service["title"],
            description=service["description"],
            cost=service["cost"],
            currency=service["currency"],
            user_login=service["user_login"],
        )


@dataclasses.dataclass(frozen=True)
class User:
    login: str
    first_name: str
    last_name: str
    user_info: str
    contacts: str

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> User:
        return cls(
            login=row["login"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            user_info=row["user_info"],
            contacts=row["contacts"],
        )

    @classmethod
    def from_dict(cls, data: dict) -> User:
        return cls(
            login=data["login"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            user_info=data["user_info"],
            contacts=data["contacts"],
        )
