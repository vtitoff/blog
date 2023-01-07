import typing as tp
from app.context import AppContext
from app import models


async def get_all_users(ctx: AppContext) -> tp.List[models.User]:
    sql = """
    select login, first_name, last_name, user_info, services from users order by login
    """
    rows = await ctx.db.fetch(sql)
    return [models.User.from_db(row) for row in rows]


async def create_user(ctx: AppContext, **kwargs) -> tp.Optional[models.User]:
    sql = """
        INSERT INTO users (login, first_name, last_name, user_info, services) VALUES
        ($1, $2, $3, $4, $5)
        """
    row = await ctx.db.fetch(
        sql,
        kwargs["login"],
        kwargs["first_name"],
        kwargs["last_name"],
        kwargs["user_info"],
        str(kwargs["services"]),
    )
    user_dict = {
        "login": kwargs["login"],
        "first_name": kwargs["first_name"],
        "last_name": kwargs["last_name"],
        "user_info": kwargs["user_info"],
        "services": kwargs["services"],
    }
    return models.User.from_dict(user_dict)
