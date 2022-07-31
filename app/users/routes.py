from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
@users.route('/register', methods=['POST'])
def register():
    print("Got request")
    return jsonify({
        "id": 1,
        "firstName": "Linn Khant",
        "lastName": "Thu",
        "mail": "linn@gmail.com"
    })
