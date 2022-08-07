from app import create_app, socketio
from flask_socketio import emit

from app.inventory.models import Product
from app.users.models import User

app = create_app()

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
