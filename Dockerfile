FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y default-libmysqlclient-dev

COPY . .

EXPOSE 5000 

ENV MYSQL_HOST=localhost
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root
ENV MYSQL_DB=pessoa

RUN apt-get update && apt-get install -y default-mysql-client

EXPOSE 80

COPY ./sql/create_schema.sql create_schema.sql
RUN mysql --host=$MYSQL_HOST --user=$MYSQL_USER --password=$MYSQL_PASSWORD < create_schema.sql

EXPOSE 5000 

CMD flask run --host=0.0.0.0 --port=5000