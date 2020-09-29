from app import db

from app.helpers.base_mixin import BaseMixin


class Token(db.Model, BaseMixin):
    __tablename__ = "tokens"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.String(255), nullable=False)

    service_id = db.Column(db.ForeignKey(("services.id")), nullable=False, index=True)
    service = db.relationship("Service", uselist=False, back_populates="tokens")
