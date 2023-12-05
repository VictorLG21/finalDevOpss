FROM python:3.8

WORKDIR /app

# Instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Instale o driver MySQL
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Copie o código fonte
COPY . .

# Configuração do banco de dados MySQL (atualize conforme necessário)
ENV MYSQL_HOST=seu_host_mysql
ENV MYSQL_USER=seu_usuario_mysql
ENV MYSQL_PASSWORD=sua_senha_mysql
ENV MYSQL_DB=seu_banco_de_dados

# Adicione a criação do esquema e tabela
COPY create_schema.sql create_schema.sql
RUN mysql --host=$MYSQL_HOST --user=$MYSQL_USER --password=$MYSQL_PASSWORD < create_schema.sql

CMD ["python", "app.py"]