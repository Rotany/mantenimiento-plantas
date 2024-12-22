from flask import Flask
from flask_cors import CORS, cross_origin
from app.config import Config
from app.models import db
from app.routes import image_bp


    

def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_bp)
    CORS(app, support_credentials=True)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

