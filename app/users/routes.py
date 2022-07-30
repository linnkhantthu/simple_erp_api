from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
@users.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    data["id"] = 1
    return data
