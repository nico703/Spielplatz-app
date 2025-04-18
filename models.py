from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<{self.name} bringt {self.item} mit>"