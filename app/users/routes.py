from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
@users.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify(data)
