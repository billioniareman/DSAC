from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Membership(db.Model):
    name = db.Column(db.String, nullable=False)
    enrollment = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    branch = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    interest = db.Column(db.String, nullable=False)
    reason = db.Column(db.String, nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    subject = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)



class Blog(db.Model):
    blogid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    author_designation = db.Column(db.String, nullable=False)



