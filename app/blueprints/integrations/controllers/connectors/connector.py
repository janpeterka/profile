from app.blueprints.auth.models.users import User


class Connector:
    def __init__(self, secret_key):
        self.user = User.load_by_attribute("secret_key", secret_key)

        if self.user is None:
            raise ValueError("wrong secret key")
