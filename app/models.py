from __future__ import annotations
import dataclasses
import asyncpg
from app import dto


@dataclasses.dataclass(frozen=True)
class Service:
    name: str
    cost: float
    currency: str

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Service:
        return cls(
            name=row['name'],
            cost=row['cost'],
            currency=row['currency'],
        )


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
            login=row['login'],
            first_name=row['first_name'],
            last_name=row['last_name'],
            user_info=row['user_info'],
            services=row['services'], #TODO разбить на итерацию
        )
