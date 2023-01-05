import typing as tp
from app.context import AppContext
from app import models


async def get_all_users(ctx: AppContext) -> tp.List[models.User]:
    sql = '''
    select login, first_name, last_name, user_info, services from users order by login
    '''
    rows = await ctx.db.fetch(sql)
    return [models.User.from_db(row) for row in rows]
