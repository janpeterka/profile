from app import db


user_tokens = db.Table(
    "user_tokens",
    db.Column("user_id", db.BigInteger, db.ForeignKey("users.id")),
    db.Column("token_id", db.BigInteger, db.ForeignKey("tokens.id")),
)
