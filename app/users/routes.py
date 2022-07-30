from flask import Blueprint, jsonify

users = Blueprint('users', __name__)

@users.route('/')
@users.route('login')
def login():
    return jsonify("userId", 1)