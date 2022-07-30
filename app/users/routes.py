from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)


@users.route('/', methods=['POST'])
@users.route('/register', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    return jsonify(data)
