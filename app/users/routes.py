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


@users.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(mail=data['mail']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        response = {
            "id": user.id,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "mail": user.mail
        }
    else:
        return Response({"message": "Mail or Password is incorrect"}, 400)
    return response
