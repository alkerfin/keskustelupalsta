from app import db
class Settings(db.Model)
	keyname = db.Column(db.String(40),primary_key=True)
	keyvalue = db.Column(db.String(40),nullable=False)
	
	def __init__(self,keyname,keyvalue):
		self.keyname = keyname
		self.keyvalue = keyvalue
