from vkbottle.bot import Blueprint, Message

from source.keyboards import HOME_KEYBOARD
from source.messages import BACK_TO_HOME_MESSAGE

bp = Blueprint("Back to keyboards")


@bp.on.private_message(payload={"command": "back_to_home"})
async def back_to_home_handler(_: Message) -> dict:
    return {"message": BACK_TO_HOME_MESSAGE, "keyboard": HOME_KEYBOARD}
