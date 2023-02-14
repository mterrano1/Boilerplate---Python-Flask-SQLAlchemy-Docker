import os
import jwt
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
# Configures the database URI for SQLAlchemy from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# Initializes SQLAlchemy and Flask-Migrate extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Enables Cross-Origin Resource Sharing (CORS) for the Flask app
CORS(app)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)


# Authenticates a user using a JSON Web Token (JWT)
def authenticate_user(request):
    # Extracts the JWT from the Authorization header
    token = request.headers.get("Authorization", None)
    if not token:
        return None
    try:
        # Decodes the JWT using the JWT_SECRET environment variable
        decoded_token = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        # Extracts the user_id from the decoded token
        user_id = decoded_token.get("user_id", None)
        if not user_id:
            # Returns None if the user_id is missing from the token
            return None
        # Returns the user_id if authentication succeeds
        return user_id
    except jwt.exceptions.DecodeError:
        # Returns None if the JWT is invalid
        return None


# Defines the GET and POST routes for the comments API
@app.route("/comments/<int:case_id>", methods=["GET", "POST"])
# Authenticates the user before proceeding
def comments(case_id=None):
    user_id = authenticate_user(request)
    # Returns an error message if authentication fails
    if not user_id:
        return jsonify({"errors": ["Not authorized"]}), 401

    if request.method == "GET":
        # Fetches all comments associated with the given case_id
        comments = Comment.query.filter_by(case_id=case_id).all()
        # Converts the comments to a list of dictionaries for JSON serialization
        comments_list = [{
            "id": comment.id,
            "case_id": comment.case_id,
            "comment": comment.comment,
            "first_name": comment.first_name,
            "last_name": comment.last_name
        } for comment in comments]
        # Returns the comments list as a JSON response
        return jsonify(comments_list)

    if request.method == "POST":
        # Save a new comment to the database
        comment_data = request.get_json()
        comment = comment_data.get("comment")
        if not comment or comment.strip() == "":
            # Returns an error message if the comment is missing or empty
            return jsonify({"errors": ["Comment is required"]}), 400
        new_comment = Comment(
            case_id=comment_data["case_id"],
            comment=comment,
            first_name=comment_data["first_name"],
            last_name=comment_data["last_name"]
        )
        # Adds the new comment to the database and commits the transaction
        db.session.add(new_comment)
        db.session.commit()
        # Returns a success message as a JSON response
        return jsonify({"message": "Comment added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)