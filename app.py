import os
from flask import Flask
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

app = Flask(__name__)
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)


@app.route("/")
def hello():
    return "Hello, World!"