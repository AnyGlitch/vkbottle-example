from vkbottle.bot import Bot

from source.blueprints import blueprints
from source.config import GROUP_TOKEN
from source.database import engine
from source.middlewares import middlewares


class App:
    __slots__ = "bot"

    def __init__(self) -> None:
        self.bot = Bot(GROUP_TOKEN)

    def set_database(self) -> None:
        self.bot.loop_wrapper.on_startup.append(engine.init())

    def set_blueprints(self) -> None:
        for blueprint in blueprints:
            blueprint.load(self.bot)

    def set_middlewares(self) -> None:
        for middleware in middlewares:
            self.bot.labeler.message_view.register_middleware(middleware)

    def run(self) -> None:
        self.set_database()
        self.set_blueprints()
        self.set_middlewares()
        self.bot.run_forever()
