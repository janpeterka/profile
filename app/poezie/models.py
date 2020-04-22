import datetime

from app import db


class Poezie(db.Model):
    __tablename__ = "poezie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    created_by = db.Column(db.String(255))

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()

    @staticmethod
    def load(id):
        item = db.session.query(Poezie).filter(Poezie.id == id).first()
        return item
