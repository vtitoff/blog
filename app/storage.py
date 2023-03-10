import typing as tp
from app.context import AppContext
from app import models
from app.constants import USERS_TABLE, SERVICES_TABLE


async def get_all_users(ctx: AppContext, page, page_limit) -> tp.List[models.User]:
    sql = f"""
    select 
        login, 
        first_name, 
        last_name, 
        user_info, 
        contacts,
        registered,
        last_activity,
        country,
        city,
        gender,
        rating,
        avatar_path
        from {USERS_TABLE} 
        order by login
        OFFSET {page*page_limit}
        LIMIT {page_limit}
    """
    rows = await ctx.db.fetch(sql)
    return [models.User.from_db(row) for row in rows]


async def get_user(ctx: AppContext, login: str) -> tp.Optional[models.User]:
    sql = f"""
    select  login, 
            first_name, 
            last_name, 
            user_info, 
            contacts, 
            registered,
            last_activity,
            country,
            city,
            gender,
            rating,
            avatar_path
    from {USERS_TABLE} where login = $1
    """
    row = await ctx.db.fetchrow(sql, login)
    return models.User.from_db(row) if row else None


async def create_user(ctx: AppContext, **kwargs) -> bool:
    sql = f"""
        INSERT INTO {USERS_TABLE} (
            login, 
            first_name, 
            last_name, 
            user_info, 
            contacts, 
            registered,
            last_activity,
            country,
            city,
            gender,
            rating,
            avatar_path) VALUES
        ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)
        """
    await ctx.db.fetch(
        sql,
        kwargs["login"],
        kwargs["first_name"],
        kwargs["last_name"],
        kwargs["user_info"],
        kwargs["contacts"],
        kwargs["registered"],
        kwargs["last_activity"],
        kwargs["country"],
        kwargs["city"],
        kwargs["gender"],
        kwargs["rating"],
        kwargs["avatar_path"],
    )
    return True


async def update_users_field(
    ctx: AppContext, login: str, field: tp.Any, value: tp.Any
) -> tp.Optional[models.User]:
    sql = f"""
        UPDATE {USERS_TABLE}
        SET {field} = $1
        WHERE login = $2;
        """
    row = await ctx.db.fetch(
        sql,
        value,
        login,
    )
    return row


async def delete_user(ctx: AppContext, login: str) -> bool:
    sql = f"""
    delete from {USERS_TABLE} 
    where login = $1
    """
    row = await ctx.db.execute(sql, login)
    return True


async def get_services_by_login(
    ctx: AppContext, login: str
) -> tp.Optional[models.User]:
    sql = f"""
    select id, title, description, cost, currency, user_login from {SERVICES_TABLE} where user_login = $1
    """
    rows = await ctx.db.fetch(sql, login)
    return [models.Service.from_db(row) for row in rows]


async def count_all(ctx: AppContext, tablename) -> int:
    sql = f"""
    select count(*) from {tablename}
    """
    row = await ctx.db.fetchrow(sql)
    return row[0]
