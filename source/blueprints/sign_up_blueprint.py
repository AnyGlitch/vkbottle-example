from vkbottle.bot import Blueprint, Message

from source.database.models import UserModel
from source.keyboards import HOME_KEYBOARD

bp = Blueprint("User sign up")


@bp.on.private_message(command="start")
@bp.on.private_message(payload={"command": "start"})
async def sign_up_handler(message: Message, user_exists: bool) -> str | dict:
    if user_exists:
        return "You have already been previously registered..."

    await UserModel.create(id=message.from_id)
    return {"message": "Welcome!", "keyboard": HOME_KEYBOARD}
