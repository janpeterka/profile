from app.bunkrs.routes import bunkrs_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(bunkrs_blueprint)
