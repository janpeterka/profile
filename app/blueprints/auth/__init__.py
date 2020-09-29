from .controllers.auth import auth_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(auth_blueprint)
