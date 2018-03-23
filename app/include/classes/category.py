from app import db
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    topic = db.Column(db.String(40),nullable=False)
    description = db.Column(db.String(144),nullable=False)
    parent = db.Column(db.Integer)
    def __init__(self,topic,description,parentid):
        self.topic = topic
        self.description = description
        self.parent = parentid
