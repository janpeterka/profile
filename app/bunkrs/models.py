import datetime

from app import db


class Bunkr(db.Model):
    __tablename__ = 'bunkrs'

    name = db.Column(db.String(255), primary_key=True)
    sale_date = db.Column(db.String(255))

    link = db.Column(db.String(255))

    katastr = db.Column(db.String(255))
    obec = db.Column(db.String(255))
    kraj = db.Column(db.String(255))
    uzemi = db.Column(db.String(255))

    min_sale_price = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    offer_type = db.Column(db.String(45))

    @staticmethod
    def load(name):
        bunkr = db.session.query(Bunkr).filter(Bunkr.name == name).first()
        return bunkr

    @staticmethod
    def load_batch(offer_type=None):
        if offer_type is None:
            bunkrs = db.session.query(Bunkr).all()
        else:
            bunkrs = db.session.query(Bunkr).filter(Bunkr.offer_type == offer_type).all()
        return bunkrs

    # @staticmethod
    # def loadActiveSale():
    #     bunkrs = db.session.query(Bunkr).filter(Bunkr.offer_type == 'sale').all()
    #     return bunkrs

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()

    def edit(self):
        try:
            db.session.commit()
            return True
        except Exception:
            # application.logger.error("Edit error: {}".format(e))
            return False

    # def print_bunkr(self):
    #     print(self.name)
    #     print(self.sale_date)
    #     print(self.katastr)
    #     print(self.obec)
    #     print(self.kraj)
    #     print(self.uzemi)
    #     print(self.min_sale_price)
    #     print(self.created_at)
    #     print('\n')
