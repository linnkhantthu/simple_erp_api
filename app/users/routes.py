from flask import Blueprint, request
from app.users.models import User
from app import bcrypt, db
import secrets

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
@users.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    password = bcrypt.generate_password_hash(data['password'])
    token = secrets.token_hex(16)
    db_user = User.query.filter_by(mail=data['mail']).first()
    db.session.add(user)
    if (db_user):
        response = {"status": False, "data": {"message": "User already exist"}}
    else:
        user = User(mail=data['mail'], firstName=data['firstName'],
                    lastName=data['lastName'], password=password, token=token)
        db.session.commit()
        response = {
            "status": True,
            "data": {"id": user.id,
                     "firstName": user.firstName,
                     "lastName": user.lastName,
                     "mail": user.mail}
        }
    return response


@users.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(mail=data['mail']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = data['token']
        response = {
            "status": True,
            "token": token,
            "data": {"id": user.id,
                     "firstName": user.firstName,
                     "lastName": user.lastName,
                     "mail": user.mail}
        }
    else:
        response = {"status": False, "data": {
            "message": "Mail or Password is incorrect"}}
    return response
