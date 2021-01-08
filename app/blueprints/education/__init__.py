from .controllers.education import education_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(education_blueprint)

    from .controllers import register_all_controllers  # noqa: F401

    register_all_controllers(app)
