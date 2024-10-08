from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(Config)

    from app import routes
    app.register_blueprint(routes.main)

    return app