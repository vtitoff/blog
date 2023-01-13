import typing as tp
from app.context import AppContext
from app import models


async def get_all_users(ctx: AppContext) -> tp.List[models.User]:
    sql = """
    select login, first_name, last_name, user_info, services from users order by login
    """
    rows = await ctx.db.fetch(sql)
    return [models.User.from_db(row) for row in rows]


async def get_user(ctx: AppContext, login: str) -> tp.Optional[models.User]:
    sql = """
    select login, first_name, last_name, user_info, services from users where login = $1
    """
    row = await ctx.db.fetchrow(sql, login)
    if row:
        return models.User.from_db(row)
    return None


async def create_user(ctx: AppContext, **kwargs) -> bool:
    sql = """
        INSERT INTO users (login, first_name, last_name, user_info, services) VALUES
        ($1, $2, $3, $4, $5)
        """
    await ctx.db.fetch(
        sql,
        kwargs["login"],
        kwargs["first_name"],
        kwargs["last_name"],
        kwargs["user_info"],
        str(kwargs["services"]),
    )
    return True


async def update_users_field(ctx: AppContext, login: str, field: tp.Any, value: tp.Any) -> tp.Optional[models.User]:
    sql = f"""
        UPDATE users
        SET {field} = $1
        WHERE login = $2;
        """
    row = await ctx.db.fetch(
        sql,
        value,
        login,
    )
    return row
