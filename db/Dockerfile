FROM mysql:latest

WORKDIR /db

COPY data.sql /docker-entrypoint-initdb.d
COPY db.cnf /etc/mysql/conf.d/