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
    def find_quant_of_posts_by_user(user_id):
        
        a = text("SELECT COUNT(Post.id) FROM Post"
                 " LEFT JOIN account ON account.id = Post.account_id"
                 " WHERE (account_id = :user_id)").params(user_id=user_id)
        res = db.engine.execute(a)
        b = []
        for row in res:
                b.append(row[0])
        return b[0]
	

    @staticmethod
    def find_posts_by_user(user_id):
        
        a = text("SELECT * FROM Post"
                 " LEFT JOIN account ON account.id = Post.account_id"
                 " WHERE (account_id = :user_id)").params(user_id=user_id)
        res = db.engine.execute(a)
        b = []
        for row in res:
                    if not row[1] in b:
                        b.append(row[1])

        
        return b
  
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

    
