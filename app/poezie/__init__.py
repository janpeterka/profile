from app.poezie.routes import poezie_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(poezie_blueprint)
