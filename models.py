from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Board111(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

