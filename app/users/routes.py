from flask import Blueprint, jsonify

users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
@users.route('/login', methods=['GET'])
def login():
    return jsonify("userId", 1)
