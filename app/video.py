import pafy
import sys

def inspect_video(url: str):
    url = url.replace("/watch?v=", "/embed/")
    try:
        video = pafy.new(url)
        link = url
        author = video.author
        title = video.title
        duration = video.duration
        rating = video.rating
        return [link, title, author, duration, rating]
    except ValueError:
        return None