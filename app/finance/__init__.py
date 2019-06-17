from app.finance.routes import finance_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(finance_blueprint)
