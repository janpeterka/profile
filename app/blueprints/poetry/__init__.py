from .controllers.poetry import poetry_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(poetry_blueprint)
