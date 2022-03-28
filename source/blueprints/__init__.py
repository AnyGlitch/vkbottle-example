from source.blueprints import about_blueprint, back_blueprint, sign_up_blueprint

blueprints = (
    about_blueprint.bp,
    back_blueprint.bp,
    sign_up_blueprint.bp,
)

__all__ = (
    "about_blueprint",
    "back_blueprint",
    "sign_up_blueprint",
)
