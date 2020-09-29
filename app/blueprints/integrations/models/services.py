from app import db

from app.helpers.base_mixin import BaseMixin


class Service(db.Model, BaseMixin):
    __tablename__ = "services"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
