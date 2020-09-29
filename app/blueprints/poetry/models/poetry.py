import datetime

from app import db


class Poetry(db.Model):
    __tablename__ = "poetry"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    created_by = db.Column(db.String(255))
    filename = db.Column(db.String(511), nullable=True)

    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()

    @staticmethod
    def load(id):
        item = db.session.query(Poetry).filter(Poetry.id == id).first()
        return item

    @staticmethod
    def load_all():
        my_objects = db.session.query(Poetry)
        return my_objects
