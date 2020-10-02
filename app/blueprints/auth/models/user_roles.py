from app import db


user_roles = db.Table(
    "user_roles",
    db.Column("user_id", db.BigInteger, db.ForeignKey("users.id")),
    db.Column("role_id", db.BigInteger, db.ForeignKey("roles.id")),
)
