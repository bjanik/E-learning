FROM python:latest

WORKDIR /app

RUN pip3 install flask flask-bcrypt flask-login psycopg2 python-dotenv pafy youtube-dl

COPY . .

CMD ["python3", "app.py"]