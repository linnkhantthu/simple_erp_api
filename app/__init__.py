from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.configs import Config
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    db.init_app(app)

    migrate = Migrate(app, db)

    from app.users.routes import users

    app.register_blueprint(users)

    return app
