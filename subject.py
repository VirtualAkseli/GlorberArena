from application import db
from sqlalchemy.sql import text

class Topic(db.Model):

        __tablename__ = "subject"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(144), nullable=False)
        posts = db.relationship("Post", backref='subject', lazy=True)
        theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'), nullable=False)
        date_created = db.Column(db.Date, default=db.func.current_timestamp())


        def __init__(self, name):

                self.name = name

        @staticmethod
        def find_matching_topic_for_post(topic_id):
            statement = text("SELECT subject.id, subject.name FROM subject"
                              " LEFT JOIN Post ON Post.subject_id = subject.id"
                              " WHERE (subject.id = :topic_id)"
                              " GROUP BY subject.id").params(topic_id=topic_id)
            result = db.engine.execute(statement)

            response = []
            for row in result:
                response.append({"id":row[0], "name":row[1]})

            return response

        
        @staticmethod
        def find_matching_topics_for_theme(theme_id):
            statement = text("SELECT subject.id, subject.name FROM subject"
                              " LEFT JOIN Theme ON Theme.id = subject.theme_id"
                              " WHERE (subject.theme_id = :theme_id)"
                              " GROUP BY subject.id").params(theme_id=theme_id)
            result = db.engine.execute(statement)

            response = []
            for row in result:
                response.append({"id":row[0], "name":row[1]})

            return response
