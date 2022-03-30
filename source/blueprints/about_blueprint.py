from vkbottle.bot import Blueprint, Message

from source.keyboards import ABOUT_PROJECT_KEYBOARD

bp = Blueprint("About many things")


@bp.on.private_message(payload={"command": "about_project"})
async def about_project_handler(_: Message) -> dict:
    return {
        "message": "About this project:",
        "keyboard": ABOUT_PROJECT_KEYBOARD,
    }
