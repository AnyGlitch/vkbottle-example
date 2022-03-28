from vkbottle import Keyboard, KeyboardButtonColor, OpenLink, Text

ABOUT_PROJECT_KEYBOARD = (
    Keyboard()
    .add(
        OpenLink("https://github.com/AnyGlitch/vkbottle-example", "Jump"),
        color=KeyboardButtonColor.SECONDARY,
    )
    .row()
    .add(
        Text(
            label="Back",
            payload={"command": "back_to_home"},
        ),
        color=KeyboardButtonColor.PRIMARY,
    )
    .get_json()
)
