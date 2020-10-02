from flask import current_app as application

from sqlalchemy.exc import DatabaseError

from app import db


# Custom methods for all classes
class BaseMixin(object):
    @classmethod
    def load(cls, *args, **kwargs):
        if "id" in kwargs:
            # e.g. Author.load(id=1)
            cls_id = kwargs["id"]
        else:
            # e.g. Author.load(1)
            cls_id = args[0]
        my_object = db.session.query(cls).filter(cls.id == cls_id).first()
        return my_object

    @classmethod
    def load_all(cls, *args, **kwargs):
        object_array = db.session.query(cls).all()
        return object_array

    @classmethod
    def load_last(cls):
        last_object = db.session.query(cls).all()[-1]
        return last_object

    @classmethod
    def load_by_name(cls, name):
        first_object = db.session.query(cls).filter(cls.name == name).first()
        return first_object

    @classmethod
    def load_by_attribute(cls, attribute, value):
        first_object = (
            db.session.query(cls).filter(getattr(cls, attribute) == value).first()
        )
        return first_object

    def edit(self, **kwargs):
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            application.logger.error("Edit error: {}".format(e))
            return False

    def save(self, **kwargs):
        """Saves (new) object
        """
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except DatabaseError as e:
            db.session.rollback()
            application.logger.error("Save error: {}".format(e))
            return False

    def remove(self, **kwargs):
        """Deletes object
        """
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except DatabaseError as e:
            db.session.rollback()
            application.logger.error("Remove error: {}".format(e))
            return False

    def expire(self, **kwargs):
        """Dumps database changes
        """
        try:
            db.session.expire(self)
            return True
        except Exception as e:
            db.session.rollback()
            application.logger.error("Expire error: {}".format(e))
            return False

    @classmethod
    def refresh(self, **kwargs):
        """Refreshed data (expires and reloads)
        """
        try:
            db.session.refresh(self)
            return True
        except Exception as e:
            db.session.rollback()
            application.logger.error("Refresh error: {}".format(e))
            return False

    # trochu hack, vraci vsechny attributes, kter nezacinaji "_" - tedy nejsou "private"
    @property
    def json(self):
        attributes = []
        for attr in self.__dict__.keys():
            if not attr.startswith("_"):
                attributes.append(attr)

        return {attr: getattr(self, attr) for attr in attributes}

    def dump(self):
        for attr in dir(self):
            print("obj.%s = %r" % (attr, getattr(self, attr)))
