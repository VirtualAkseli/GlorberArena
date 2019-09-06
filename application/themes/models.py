from application import db
from sqlalchemy.sql import text

class Theme(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(250), nullable=False)
        Topics = db.relationship("Topic", backref='theme', lazy=True)
        
        def __init__(self, name):

                self.name = name
        
        @staticmethod
        def find_name_for_theme(theme_id):
                statement = text("SELECT Theme.name FROM Theme WHERE (id = :theme_id)").params(theme_id=theme_id)

                result = db.engine.execute(statement)

                response = []
                for row in result:
                        response.append(row[0])
                
                return response
