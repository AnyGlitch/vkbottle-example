from tortoise import Tortoise

from source.config import ORM


async def init():
    await Tortoise.init(ORM)
