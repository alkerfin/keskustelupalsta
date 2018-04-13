from app import db
class Message(db.Model)
	id = db.Column(db.Integer,primary_key=True)
	cat_parent = db.Column(db.Integer)
	msg_parent = db.Column(db.Integer)
	user_id = db.Column(db.Integer)
	topic = db.Column(db.String(40))
	body = db.Column(db.String(500))

	def __init__(self,cat,msg,user,topic,body):
		self.cat_parent = cat
		self.msg_parent = msg
		self.user_id = user
		self.topic = topic	
		self.body = body
