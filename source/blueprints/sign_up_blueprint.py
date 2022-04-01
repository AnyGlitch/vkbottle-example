from vkbottle.bot import Blueprint, Message
from vkbottle.dispatch.rules.base import CommandRule, PayloadRule

from source.database.models import UserModel
from source.keyboards import HOME_KEYBOARD
from source.messages import SIGN_UP_MESSAGE, USER_EXISTS_MESSAGE

bp = Blueprint("User sign up")


@bp.on.private_message(CommandRule("start") | PayloadRule({"command": "start"}))
async def sign_up_handler(message: Message, user_exists: bool) -> str | dict:
    if user_exists:
        return USER_EXISTS_MESSAGE

    await UserModel.create(id=message.from_id)
    return {"message": SIGN_UP_MESSAGE, "keyboard": HOME_KEYBOARD}
