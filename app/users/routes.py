from flask import Blueprint, Response, jsonify, request
from app.users.models import User
from app import bcrypt, db

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
@users.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    password = bcrypt.generate_password_hash(data['password'])
    user = User(mail=data['mail'], firstName=data['firstName'],
                lastName=data['lastName'], password=password)
    db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:
        return Response({"message": e}, 400)
    response = {
        "id": user.id,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "mail": user.mail
    }
    return response
