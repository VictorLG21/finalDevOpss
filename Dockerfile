FROM python:3.8

WORKDIR /app

# Instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Instale o driver MySQL
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Copie o código fonte
COPY . .

EXPOSE 5000 

# Configuração do banco de dados MySQL (atualize conforme necessário)
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root
ENV MYSQL_DB=pessoa

# Adicione a criação do esquema e tabela
COPY ./sql/create_schema.sql create_schema.sql
RUN mysql --host=$MYSQL_HOST --user=$MYSQL_USER --password=$MYSQL_PASSWORD < create_schema.sql

EXPOSE 5000 

CMD flask run --host=0.0.0.0 --port=5000