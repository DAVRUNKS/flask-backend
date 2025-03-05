import os
from flask import Flask, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Frontend Path
dist_folder = os.path.abspath(os.path.join(os.getcwd(), "..", "frontend/vite-project", "dist"))
print(f"Serving frontend from: {dist_folder}")

if not os.path.exists(dist_folder):
    print(f"⚠️ Warning: {dist_folder} does not exist! Make sure to build your frontend.")

@app.route("/", defaults={"filename": "index.html"})
@app.route("/<path:filename>")
def index(filename):
    if not os.path.exists(dist_folder):
        return jsonify({"error": "Frontend build missing. Run `npm run build` in the frontend folder."}), 500
    
    return send_from_directory(dist_folder, filename)

# Import routes after app initialization
import routes  

# Create tables in the database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
