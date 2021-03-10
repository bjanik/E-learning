import pytest
import pafy

from .db import DB
from .video import inspect_video



def test_inspect_video(monkeypatch):
    
    class Mockvideo:
        def __init__(self, link, title, author, duration, rating):
            self.link = link
            self.title = title
            self.author = author
            self.duration = duration
            self.rating = rating

    def raise_exc():
        raise Exception

    monkeypatch.setattr(pafy, 'new', lambda _: raise_exc)
    res = inspect_video('url')
    assert res is None

    stats = ['url', 'title', 'author', '00:05:00', 5]
    monkeypatch.setattr(pafy, 'new', lambda x: Mockvideo(*stats))
    res = inspect_video('url')
    assert res == stats

    stats = ['/embed/123abc', 'title', 'author', '00:05:00', 5]
    monkeypatch.setattr(pafy, 'new', lambda x: Mockvideo(*stats))
    res = inspect_video('/watch?v=123abc')
    assert res == stats

def test_db():

    class MockDB:
        def __init__(self):
            self.connection_opened = False
            self.categories = {'Bash': 1, 'Python': 2}
            self.videos = {
                'Bash': [
                    ['url1', 'title1', 'author1', 1, '00:05:00', 5],
                    ['url2', 'title2', 'author2', 1, '00:05:00', 5],
                    ['url3', 'title3', 'author3', 1, '00:05:00', 5],

                ],
                'Python': [
                    ['url1', 'title1', 'author1', 2, '00:04:00', 4],
                    ['url2', 'title2', 'author2', 2, '00:04:00', 4],
                    ['url3', 'title3', 'author3', 2, '00:04:00', 4],
                ]
            }

        def get_categories(self):
            return ['Bash', 'Python']

        def __enter__(self):
            self.connection_opened = True
            return self

        def __exit__(self, exc_type, exc_val, traceback):
            self.connection_opened = False

    def get_videos_by_category(self, category=''):
        pass

    def insert_new_video(self, category, infos=['url4', 'title4', 'author4', '00:04:00', 4]):
        cat = self.videos.get(category)
        if cat:
            infos.insert(3, cat)





