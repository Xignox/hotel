from extension import db


class Rooms(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(255))
    status = db.Column(db.String(255))
    price = db.Column(db.Integer)
    reservation = db.relationship('Reservation', backref="rooms",lazy=True)
    

    def __init__(self, room_type, status, price):
        self.room_type = room_type 
        self.status = status
        self.price = price
       

    def store(self):
        db.session.add(self)
        return db.session.commit()




    def update(self,  room_type, status, price):
        self.room_type = room_type
        self.status = status
        self.price = price
       

        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()


        


