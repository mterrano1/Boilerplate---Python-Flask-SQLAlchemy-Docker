import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)


@app.route("/comments/<int:case_id>", methods=["GET", "POST"])
def comments(case_id=None):
    if request.method == "GET":
        # Fetch comments for a specific case
        comments = Comment.query.filter_by(case_id=case_id).all()
        comments_list = [{
            "id": comment.id,
            "case_id": comment.case_id,
            "comment": comment.comment,
            "first_name": comment.first_name,
            "last_name": comment.last_name
        } for comment in comments]
        return jsonify(comments_list)

    if request.method == "POST":
        # Save a new comment to the database
        comment_data = request.get_json()
        comment = comment_data.get("comment")
        if not comment or comment.strip() == "":
            return jsonify({"errors": ["Comment is required"]}), 400
        new_comment = Comment(
            case_id=comment_data["case_id"],
            comment=comment,
            first_name=comment_data["first_name"],
            last_name=comment_data["last_name"]
        )
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({"message": "Comment added successfully."})

if __name__ == '__main__':
    app.run(debug=True)