from tortoise import Tortoise

from source.config import ORM


async def init() -> None:
    await Tortoise.init(ORM)
