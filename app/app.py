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
    db.close_connection()
    return "Index"

@app.route("/login")
def login():
    """Simply returns the login page"""
    return "login.html"

@app.route("/categories/<string:name>")
def category(name: str):
    """Get from database all videos of <name> category"""
    db = DB("elearning")
    db.open_connection()
    categories = db.get_categories()
    videos = db.get_videos_by_category(name)
    db.close_connection()
    print(videos)
    print(categories)
    return name

@app.route("/add")
def add():
    """ Returns adding video page"""
    return "addVideo.html"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)