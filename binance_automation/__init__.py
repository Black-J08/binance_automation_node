from flask import Flask
from binance_automation.index import views


def create_app():
    app = Flask(__name__)

    app.register_blueprint(views.index_bp)

    app.config.from_pyfile('../config.py')

    return app
