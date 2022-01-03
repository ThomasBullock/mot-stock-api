from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. 
# For that reason, the extension expects that the application will configure a user loader function, that can be called to load a user given the ID.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Tranche(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol =  db.Column(db.String(6), index=True)
    price = db.Column(db.Numeric(10,3))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Tranche {}>'.format(self.body)

