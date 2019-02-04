from flask_login import UserMixin
from extension import db   
from extension import flask_login as login


@login.user_loader
def load_user(email):
    return User.query.filter_by(email = email).first()

class User(db.Model):
    __tablename__ = 'register'

    email = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password


    def __repr__(self):
        return '<User %r>' % self.email
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.email)

    def __init__(self, email, password):
        self.email = email
        self.password = password


    def store(self):
        db.session.add(self)
        return db.session.commit()

    def update(self, email, password):
        self.email = email
        self.password = password
                            

        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()


