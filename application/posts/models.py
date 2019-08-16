from application import db
from application.authentication.models import User
from application.posts import subject
from sqlalchemy.sql import text

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	topic = db.Column(db.String(144), nullable=False)
	content = db.Column(db.String(144), nullable=False)
	author = db.Column(db.String(144), nullable=False)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
	
	
	def __init__(self, content):
		
		self.topic = "Name of the topic"
		self.content = content
		self.author = "Name of the author"





















	@staticmethod
	def find_matching_topic_for_post(topic_id):
		statement = text("SELECT Post.id, Post.content, Post.author FROM Post"
				" LEFT JOIN subject ON subject.id = subject_id"
				" WHERE (subject_id = :topic_id)"
				" GROUP BY Post.id").params(topic_id=topic_id)
		result = db.engine.execute(statement)

		response = []
		for row in result:
			response.append({"id":row[0], "content":row[1], "author":row[2]})

		return response
