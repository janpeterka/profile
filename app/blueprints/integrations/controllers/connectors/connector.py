import os


class Connector:
    def __init__(self, secret_key):
        if not secret_key == os.environ.get("INTEGRATIONS_SECRET_KEY"):
            raise ValueError("wrong key")
