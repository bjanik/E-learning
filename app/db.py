import mysql.connector
import os
import sys

class DB:
    def __init__(self):
        self._dbcon = None

    def __enter__(self):
        try:
            self._dbcon = mysql.connector.connect(
                host=os.environ['AZ_POSTGRES_HOST'],
                user=os.environ['AZ_POSTGRES_USER'],
                password=os.environ['AZ_POSTGRES_PASSWORD'],
                database=os.environ['AZ_POSTGRES_DATABASE']
            )
            self._cursor = self._dbcon.cursor()
            return self
        except:
            raise

    def __exit__(self, exc_type, exc_val, traceback):
        self._dbcon.close()

    def set_tables(self, ptf):
        for line in open(ptf):
            self._cursor.execute(line)

    def get_categories(self):
        self._cursor.execute('SELECT category FROM categories')
        categories = self._cursor.fetchall()
        categories = [cat[0] for cat in categories]
        categories.sort()
        return categories

    def get_videos_by_category(self, category=''):
        if category:
            query = "SELECT link, title, category FROM videos,categories WHERE categories.ID=videos.categoryid AND category LIKE %s"
            self._cursor.execute(query, [category])
        else:
            query = f'SELECT link, title, category FROM videos,categories WHERE categories.ID=videos.categoryid LIMIT 12'
            self._cursor.execute(query)
        videos = self._cursor.fetchall()
        return videos

    def insert_new_video(self, category, infos):
        query = "SELECT ID FROM categories WHERE category LIKE %s"
        self._cursor.execute(query, [category])
        cat = self._cursor.fetchall()[0][0]
        infos.insert(3, cat)
        query = 'INSERT INTO videos (link, title, author, categoryid, duration, ranking) VALUES (%s, %s, %s, %s, %s, %s)'
        self._cursor.execute(query, tuple(infos))
        self._dbcon.commit()