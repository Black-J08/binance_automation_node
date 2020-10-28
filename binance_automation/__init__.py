from flask import Flask


def create_app():
    app = Flask(__name__)

    from binance_automation.index import views
    app.register_blueprint(views.index_bp)

    from binance_automation.login import views
    app.register_blueprint(views.login_bp)

    app.config.from_pyfile('../config.py')

    return app
