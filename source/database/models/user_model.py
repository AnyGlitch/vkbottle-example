from tortoise import Model, fields


class UserModel(Model):
    id = fields.IntField(pk=True)

    class Meta:
        table = "users"
