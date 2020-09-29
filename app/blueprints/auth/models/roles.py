from app import db

from flask_security.models.fsqla_v2 import FsRoleMixin as RoleMixin
from app.helpers.base_mixin import BaseMixin


class Role(db.Model, RoleMixin, BaseMixin):
    __tablename__ = "roles"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
