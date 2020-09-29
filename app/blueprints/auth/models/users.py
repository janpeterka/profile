from app import db

from app.helpers.base_mixin import BaseMixin

from flask_security.models.fsqla_v2 import FsUserMixin as UserMixin

from.roles import Role
from .user_roles import user_roles


class User(db.Model, BaseMixin, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    roles = db.relationship("Role", secondary="user_roles", backref="users")
    tokens = db.relationship("Token", secondary="user_tokens")
