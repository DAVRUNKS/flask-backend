from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # Initialize the database

import routes  # Import routes after initializing `app`

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
