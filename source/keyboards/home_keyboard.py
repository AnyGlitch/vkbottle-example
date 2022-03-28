from vkbottle import Keyboard, KeyboardButtonColor, Text

HOME_KEYBOARD = (
    Keyboard()
    .add(
        Text(
            label="About",
            payload={"command": "about_project"},
        ),
        color=KeyboardButtonColor.PRIMARY,
    )
    .get_json()
)
