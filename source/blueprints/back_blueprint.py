from vkbottle.bot import Blueprint, Message

from source.keyboards import HOME_KEYBOARD

bp = Blueprint("Back to keyboards")


@bp.on.private_message(payload={"command": "back_to_home"})
async def back_to_home_handler(message: Message) -> dict:
    return {"message": "Return to home page.", "keyboard": HOME_KEYBOARD}
