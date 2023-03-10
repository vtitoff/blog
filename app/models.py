from __future__ import annotations
import dataclasses
import json
import asyncpg
import typing as tp
import app.models as models
from datetime import datetime
from enum import Enum


class Gender(Enum):
    male: "male"
    female: "female"


@dataclasses.dataclass(frozen=True)
class Service:
    id: str
    title: str
    description: str
    cost: float
    currency: str
    user_login: str

    @classmethod
    def from_db(cls, row: tp.Union[asyncpg.Record, models.Service]) -> Service:
        return cls(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            cost=row["cost"],
            currency=row["currency"],
            user_login=row["user_login"],
        )

    @classmethod
    def from_request(cls, service: dict) -> tp.Optional[Service]:
        return cls(
            id=service["id"],
            title=service["title"],
            description=service["description"],
            cost=service["cost"],
            currency=service["currency"],
            user_login=service["user_login"],
        )

    @classmethod
    def to_dict(cls, service: models.Service) -> dict:
        return {
            "id": str(service.id),
            "title": service.title,
            "description": service.description,
            "cost": service.cost,
            "currency": service.currency,
            "user_login": service.user_login,
        }


@dataclasses.dataclass(frozen=True)
class User:
    login: str
    first_name: str
    last_name: str
    user_info: str
    contacts: str
    registered: datetime
    last_activity: datetime
    country: str
    city: str
    gender: Gender
    rating: float
    avatar_path: str

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> User:
        return cls(
            login=row["login"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            user_info=row["user_info"],
            contacts=row["contacts"],
            registered=row["registered"],
            last_activity=row["last_activity"],
            country=row["country"],
            city=row["city"],
            gender=row["gender"],
            rating=row["rating"],
            avatar_path=row["avatar_path"]
        )

    @classmethod
    def from_dict(cls, data: dict) -> User:
        return cls(
            login=data["login"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            user_info=data["user_info"],
            contacts=data["contacts"],
            registered=data["registered"],
            last_activity=data["last_activity"],
            country=data["country"],
            city=data["city"],
            gender=data["gender"],
            rating=data["rating"],
            avatar_path=data["avatar_path"]
        )
