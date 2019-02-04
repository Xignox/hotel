from extension import db
                

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rooms_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    date_in = db.Column(db.DateTime)
    date_out = db.Column(db.DateTime)
    child_count = db.Column(db.Integer)
    adult_count = db.Column(db.Integer)


    def __init__(self, users_id, rooms_id, date_in, date_out, child_count, adult_count):
        self.users_id = users_id
        self.rooms_id = rooms_id
        self.date_in = date_in
        self.date_out = date_out
        self.child_count = child_count
        self.adult_count = adult_count
        
    def store(self):
        db.session.add(self)
        return db.session.commit()


    def update(self, users_id, rooms_id, date_in, date_out, child_count, adult_count):
        self.users_id = users_id
        self.rooms_id = rooms_id
        self.date_in = date_in
        self.date_out = date_out
        self.child_count = child_count
        self.adult_count = adult_count
        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()



