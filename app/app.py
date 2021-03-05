import logging
import os
import sys
import logging

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)
from logger import log
from db import DB
from video import inspect_video

logging.basicConfig(filename="LOG_elearning.log",
                    filemode="a",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')


app = Flask(__name__)


@app.route("/")
@log
def index():
    with DB() as db:
        videos = db.get_videos_by_category()
        categories = db.get_categories()
    return render_template("index.html", categories=categories, videos=videos)

@app.route("/login")
@log
def login():
    db.set_tables('db.py')
    """Simply returns the login page"""
    return render_template("login.html")

@app.route("/categories/<string:name>")
@log
def category(name: str):
    """Get from database all videos of <name> category"""
    with DB() as db:
        categories = db.get_categories()
        videos = db.get_videos_by_category(name)
    return render_template('index.html', categories=categories, videos=videos)

@app.route("/new_user", methods=["POST"])
@log
def new_user():
    pass

@app.route("/new_video", methods=["POST"])
@log
def new_video():
    link = request.form.get('link')
    category = request.form.get('cat')
    infos = inspect_video(link)
    try:
        with DB() as db:
            categories = db.get_categories()
            db.insert_new_video(category, infos)
            message = 'Video was successfully added'
    except Exception as e:
        message = 'Failed to add video'
    finally:
        return render_template("addVideo.html", categories=categories, message=message)

@app.route("/add")
@log
def add():
    """ Returns adding video page"""
    with DB() as db:
        categories = db.get_categories()
    return render_template("addVideo.html", categories=categories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['FLASK_RUN_PORT'], debug=True)