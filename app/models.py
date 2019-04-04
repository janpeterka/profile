import datetime

from app import db
import sqlite3


def create_database():
    conn = sqlite3.connect('db/bunkrs.db')
    c = conn.cursor()

    c.execute('''
              CREATE TABLE bunkrs
                (
                    name varchar(255) PRIMARY KEY ASC,
                    sale_date varchar(255),
                    katastr varchar(255),
                    obec varchar(255),
                    kraj varchar(255),
                    uzemi varchar(255),
                    min_sale_price integer,
                    created_at datetime
                )
              ''')

    conn.commit()
    conn.close()
    print('Database created.')


class Bunkr(db.Model):
    __tablename__ = 'bunkrs'

    name = db.Column(db.String(255), primary_key=True)
    sale_date = db.Column(db.String(255))

    katastr = db.Column(db.String(255))
    obec = db.Column(db.String(255))
    kraj = db.Column(db.String(255))
    uzemi = db.Column(db.String(255))

    min_sale_price = db.Column(db.Integer)

    created_at = db.Column(db.Date(), default=datetime.datetime.now)

    @staticmethod
    def load(name):
        bunkr = db.session.query(Bunkr).filter(Bunkr.name == name).first()
        return bunkr

    @staticmethod
    def loadAll():
        bunkrs = db.session.query(Bunkr).all()
        return bunkrs

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()

    def print_bunkr(self):
        print(self.name)
        print(self.sale_date)
        print(self.katastr)
        print(self.obec)
        print(self.kraj)
        print(self.uzemi)
        print(self.min_sale_price)
        print(self.created_at)
        print('\n')


class Folder(object):
    def __init__(self, path, name=None):
        self.path = path
        self.name = name


def main():
    try:
        create_database()
    except Exception:
        pass


main()
