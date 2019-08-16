from application import db

from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean(False))

    posts = db.relationship("Post", backref='account', lazy=True)

    def __init__(self, name):
       
        self.name = name
        
    @staticmethod
    def find_quant_of_posts_by_user():
        a = text("SELECT account.id, COUNT(Post.id) FROM account"
                 " LEFT JOIN Post ON Post.account_id = account.id"
                 " GROUP BY account.id")
        res = db.engine.execute(a)

        return res
	
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_name(self):
        return self.name


