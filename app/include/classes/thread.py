from app import db
class Thread(db.Model):
	id = db.Column(db.Integer,autoincrement=True,primary_key=True)
	cat_id = db.Column(db.Integer)
	header = db.Column(db.String(40))
	body = db.Column(db.String(500))

	def __init__(self,id,cat,header,body):
		self.cat_id = cat
		self.header = header
		self.body = body
