# models.py

from flask_login import UserMixin
from . import db

# def class
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    bgcode = db.Column(db.String(100))
# end def

# def class
class Gita(db.Model):
    __tablename__ = "gita"
    id = db.Column(db.Integer, primary_key = True)
    origchapternum = db.Column(db.Numeric(7,3))
    origchapter = db.Column(db.String(120))
    origid = db.Column(db.Integer)
    sanskrit1 = db.Column(db.String(254))
    sanskrit2 = db.Column(db.String(254))
    sanskrit3 = db.Column(db.String(254))
    sanskrit4 = db.Column(db.String(254))
    sanskrit5 = db.Column(db.String(254))
    sanskrit6 = db.Column(db.String(254))
    sanskrit_main = db.Column(db.String(254))
    trasliter_my = db.Column(db.String(254))
    purpose_my = db.Column(db.String(254))
    user = db.Column(db.String(254))
    
    def __repr__(self):
        return "<Gita(origchapternum='%s', origid='%d', sanskrit_main='%s')>" % (
            self.origchapternum, self.origid, self.sanskrit_main)
# end def

    