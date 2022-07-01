from typing import Literal

from vkbottle.bot import Blueprint, Message
from vkbottle.dispatch.rules.base import PayloadRule

from source.keyboards import ABOUT_PROJECT_KEYBOARD
from source.messages import ABOUT_PROJECT_MESSAGE

bp = Blueprint("About many things")

AboutProjectHandlerReturn = dict[Literal["message"] | Literal["keyboard"], str]


@bp.on.private_message(PayloadRule({"command": "about_project"}))
async def about_project_handler(_: Message) -> AboutProjectHandlerReturn:
    return {
        "message": ABOUT_PROJECT_MESSAGE,
        "keyboard": ABOUT_PROJECT_KEYBOARD,
    }
