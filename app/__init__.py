from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.configs import Config
from flask_migrate import Migrate
from flask_socketio import SocketIO

db = SQLAlchemy()
bcrypt = Bcrypt()
socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")

    migrate = Migrate(app, db)

    from app.users.routes import users
    from app.inventory.routes import inventory

    app.register_blueprint(users)
    app.register_blueprint(inventory)

    return app
