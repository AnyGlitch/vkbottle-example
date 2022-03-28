import decouple

GROUP_TOKEN = decouple.config("GROUP_TOKEN")
DATABASE_URL = decouple.config("DATABASE_URL")

ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ("source.database.models", "aerich.models"),
            "default_connection": "default",
        }
    },
}
