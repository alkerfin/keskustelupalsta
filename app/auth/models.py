from app import db

class User(db.Model):
    __tablename__ = "account"


    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.Integer,default=0)
    email = db.Column(db.String(144),nullable=False)
    salt = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    #TODO : To use role AND roleRules database table
    def is_allowed_object(self,obj):
        cHelper = CrudHelper(self.id)
        return cHelper.isAllowed(obj)

    def is_authenticated(self):
        return True
