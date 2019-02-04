from extension import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))


    def __init__(self, name, description):
        self.name = name 
        self.description = description


    def store(self):
        db.session.add(self)
        return db.session.commit()




    def update(self, name, description):
        self.name = name
        self.description = description


        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()