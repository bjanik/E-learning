import os

from flask import (
    Flask,
    jsonify,
    render_template
)

from db import DB

app = Flask(__name__)

@app.route("/")
def index():
    db = DB("elearning")
    db.open_connection()
    videos = db.get_videos_by_category()
    categories = db.get_categories()
    db.close_connection()
    return render_template("index.html", categories=categories, videos=videos)

@app.route("/login")
def login():
    """Simply returns the login page"""
    return render_template("login.html")

@app.route("/categories/<string:name>")
def category(name: str):
    """Get from database all videos of <name> category"""
    db = DB("elearning")
    db.open_connection()
    categories = db.get_categories()
    videos = db.get_videos_by_category(name)
    db.close_connection()
    return render_template('index.html', categories=categories, videos=videos)

@app.route("/new_user", methods=["POST"])
def new_user():
    pass

@app.route("/add")
def add():
    """ Returns adding video page"""
    return render_template("addVideo.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['FLASK_RUN_PORT'], debug=True)