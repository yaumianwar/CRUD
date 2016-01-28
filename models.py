from db import database


class Polls(database.Model):
    __tablename__ = 'polls'

    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50))
    candidate = database.Column(database.String(50))
    createdtime = database.Column(database.DateTime)


    def __init__(self, name, candidate):
        self.name = name
        self.candidate = candidate

    def __repr__(self):
        return '<Polls {}>'.format(self.name)
