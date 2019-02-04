from flask_login import UserMixin
from extension import db   
from extension import flask_login as login
from datetime import datetime


@login.user_loader
def load_user(email):
    return User.query.filter_by(email = email).first()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    middlename = db.Column(db.String(255))
    address = db.Column(db.String(225))
    mobile = db.Column(db.Integer)
    role = db.Column(db.String(255))
    email = db.Column(db.String(225),unique=True)
    password = db.Column(db.String(150))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    reservation = db.relationship('Reservation', backref="users",lazy=True)
    #reservation = db.relationship('Reservation', backref="user",lazy=True)
    #schedules = db.relationship('Schedule', backref="user",lazy=True)
    #repairs = db.relationship('Repair', backref="user",lazy=True)



    def __init__(self, firstname, lastname, middlename, address, mobile,email,role,password):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.address = address
        self.mobile = mobile
        self.email = email
        self.role = role
        self.password = password
       #self.created_at = created_at
        #self.updated_at = updated_at

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

    def __init__(self, firstname, lastname, middlename, address, mobile, email, role, password,):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.address = address
        self.mobile = mobile
        self.email = email
        self.role = role
        self.password = password
        #self.created_at = created_at
        #self.updated_at =  updated_at
        
    def store(self):
        db.session.add(self)
        return db.session.commit() 


    def update(self, firstname, lastname, middlename, address, mobile, email, role,password):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.address = address
        self.mobile = mobile
        self.email = email
        self.role = role
        self.password = password

       
       

        return db.session.commit()



    def delete(self):
        db.session.delete(self)
        return db.session.commit()


