from vkbottle.bot import Blueprint, Message

from source.keyboards import ABOUT_PROJECT_KEYBOARD
from source.messages import ABOUT_PROJECT_MESSAGE

bp = Blueprint("About many things")


@bp.on.private_message(payload={"command": "about_project"})
async def about_project_handler(_: Message) -> dict:
    return {
        "message": ABOUT_PROJECT_MESSAGE,
        "keyboard": ABOUT_PROJECT_KEYBOARD,
    }
