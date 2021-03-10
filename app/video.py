import pafy
import sys

from .logger import log


@log
def inspect_video(url: str):
    try:
        if '&' in url:
            url = url.split('&')[0]
        video = pafy.new(url)
        link = url.replace("/watch?v=", "/embed/")
        author = video.author
        title = video.title
        duration = video.duration
        rating = round(video.rating, 2)
        return [link, title, author, duration, rating]
    except:
        return None