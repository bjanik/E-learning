import mysql.connector
import os

class DB:
    def __init__(self, db_name):
        self._db_name = db_name
        self._dbcon = None

    def open_connection(self):
        self._dbcon = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            auth_plugin='mysql_native_password',
            database=os.environ['MYSQL_DATABASE']
        )
        self._cursor = self._dbcon.cursor()

    def close_connection(self):
        self._dbcon.close()
        self._dbcon = None

    def get_categories(self):
        query = 'SELECT category FROM categories'
        self._cursor.execute(query)
        categories = self._cursor.fetchall()
        categories = [cat[0] for cat in categories]
        categories.sort()
        return categories

    def get_videos_by_category(self, category=''):
        if category:
            query = f'SELECT link, title, category FROM videos,categories WHERE categories.ID=videos.categoryid AND category LIKE "{category}"'
        else:
            query = f'SELECT link, title, category FROM videos,categories WHERE categories.ID=videos.categoryid LIMIT 12'
        self._cursor.execute(query)
        videos = self._cursor.fetchall()
        return videos

