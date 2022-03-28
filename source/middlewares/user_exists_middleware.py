from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from source.database.models import UserModel


class UserExistsMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        self.send(
            {"user_exists": await UserModel.exists(id=self.event.from_id)}
        )
