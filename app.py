from flask import Flask
from flask_restx  import Api,swagger
from model.pessoa import init_app, db
from routes.pessoa import bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/pessoa'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    app.register_blueprint(bp)



    init_app(app) 
    
    with app.app_context():
        db.create_all()
    return app
 
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)