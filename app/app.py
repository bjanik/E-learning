import logging
import os
import sys

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)

from db import DB
from video import inspect_video

app = Flask(__name__)

@app.route("/")
def index():
    with DB() as db:
        videos = db.get_videos_by_category()
        categories = db.get_categories()
    return render_template("index.html", categories=categories, videos=videos)

@app.route("/login")
def login():
    """Simply returns the login page"""
    return render_template("login.html")

@app.route("/categories/<string:name>")
def category(name: str):
    """Get from database all videos of <name> category"""
    with DB() as db:
        categories = db.get_categories()
        videos = db.get_videos_by_category(name)
    return render_template('index.html', categories=categories, videos=videos)

@app.route("/new_user", methods=["POST"])
def new_user():
    pass

@app.route("/new_video", methods=["POST"])
def new_video():
    link = request.form['link']
    category = request.form['cat']
    infos = inspect_video(link)
    try:
        with DB() as db:
            categories = db.get_categories()
            db.insert_new_video(category, infos)
            message = 'Video was successfully added'
    except:
        message = 'Failed to add video'
    finally:
        return render_template("addVideo.html", categories=categories, message=message)

@app.route("/add")
def add():
    """ Returns adding video page"""
    with DB() as db:
        categories = db.get_categories()
    return render_template("addVideo.html", categories=categories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['FLASK_RUN_PORT'], debug=True)