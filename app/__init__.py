from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.configs import Config
from flask_migrate import Migrate
from flask_sock import Sock

db = SQLAlchemy()
bcrypt = Bcrypt()
sock = Sock()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    sock.init_app(app)
    migrate = Migrate(app, db)

    from app.users.routes import users
    from app.inventory.routes import inventory
    from app.inventory.routes import _sock

    sock.bp.register_blueprint(_sock)
    app.register_blueprint(users)
    app.register_blueprint(inventory)

    return app
