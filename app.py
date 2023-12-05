from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from model.pessoa import init_app, db
from routes.pessoa import pessoa_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/pessoa'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    api = Api(app)
    swagger = Swagger(app)

    init_app(app)  # Não precisa passar a instância do db aqui
    app.register_blueprint(pessoa_bp, url_prefix='/api')

    
    with app.app_context():
        db.create_all()
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)