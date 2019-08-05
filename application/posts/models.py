from application import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	topic = db.Column(db.String(144), nullable=False)
	content = db.Column(db.String(144), nullable=False)
	author = db.Column(db.String(144), nullable=False)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	
	def __init__(self, content):
		
		self.topic = "Name of the topic"
		self.content = content
		self.author = "Name of the author"
		
