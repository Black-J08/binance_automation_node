from flask import Flask
from pathlib import Path


def create_app():
    app = Flask(__name__, root_path=Path(__file__).resolve().parent.parent)

    from binance_automation.index import views
    app.register_blueprint(views.index_bp)

    from binance_automation.login import views
    app.register_blueprint(views.login_bp)

    app.config.from_pyfile('config.py')

    return app
