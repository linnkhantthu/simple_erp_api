from flask import Blueprint, jsonify, request
from app.inventory.models import Product
from app.users.models import User

inventory = Blueprint('inventory', __name__)


@inventory.route('/inventory', methods=['POST'])
def products():
    data = request.get_json()
    user = User.query.filter_by(mail=data['mail']).first()
    if user:
        response = {
            "status": True,
            "data": [],
        }
        products = Product.query.filter_by(owner=user)
        for product in products:
            response["data"].append({"id": int(product.id),
                                     "productName": product.productName,
                                     "contains": int(product.contains),
                                     "unit": product.unit,
                                     "price": float(product.price),
                                     "qty": int(product.qty)}
                                    )
        return jsonify(response)
    else:
        response = {"status": False, "data": {
            "message": "You don't have access to this page"}}
    return response


@inventory.route('/getUnits', methods=['POST'])
def getUnits():
    data = request.get_json()
    user = User.query.filter_by(mail=data['mail']).first()
    if user:
        response = {
            "status": True,
            "data": ["PCS", "KG", "G"],
        }
        return jsonify(response)
    else:
        response = {"status": False, "data": {
            "message": "You don't have access to this page"}}
    return response
