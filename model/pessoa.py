from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    idade = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
        }

def init_app(app):
    if not app.config.get('SQLALCHEMY_DATABASE_URI'):
        raise ValueError("SQLALCHEMY_DATABASE_URI não está configurado no app")

    db.init_app(app)

    with app.app_context():
        db.create_all()