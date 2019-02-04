from extension import db


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    mode = db.Column(db.String(255))
    reserve_id = db.Column(db.Integer)

    def __init__(self, firstname, lastname, mode, reserve_id):
        self.firstname = firstname 
        self.lastname = lastname
        self.mode = mode
        self.reserve_id = reserve_id



    def store(self):
        db.session.add(self)
        return db.session.commit()


    def update(self, firstname, lastname, mode, reserve_id):
        self.firstname = firstname
        self.lastname = lastname
        self.mode = mode
        self.reserve_id = reserve_id

        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()