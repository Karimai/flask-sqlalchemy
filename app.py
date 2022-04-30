from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User: {self.email}> "

if __name__ == "__main__":
    app.run()

