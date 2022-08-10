from flask import Blueprint, jsonify, request
from app.inventory.models import Product
from app.users.models import User
from flask_socketio import emit
from app import socketio

inventory = Blueprint('inventory', __name__)


@inventory.route('/inventory', methods=['POST'])
def products():
    dummyProductList = [
        {
            "id": 1,
            "productName": "Hat",
            "contains": 100,
            "unit": "PCS",
            "price": 2500.0,
            "qty": 200,
        },
        {
            "id": 2,
            "productName": "Shoes",
            "contains": 50,
            "unit": "PCS",
            "price": 25000.0,
            "qty": 150,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
        {
            "id": 1,
            "productName": "iPad",
            "contains": 1,
            "unit": "PCS",
            "price": 1100000.0,
            "qty": 5,
        },
    ]
    data = request.get_json()
    user = User.query.filter_by(mail=data['mail']).first()
    if user:
        response = {
            "status": True,
            "data": [],
        }
        products = Product.query.filter_by(owner=user)
        for product in dummyProductList:
            response["data"].append({"id": product['id'],
                                     "productName": product['productName'],
                                     "contains": product['contains'],
                                     "unit": product['unit'],
                                     "price": product['price'],
                                     "qty": product['qty']}
                                    )
        return jsonify(response)
    else:
        response = {"status": False, "data": {
            "message": "You don't have access to this page"}}
    return response


@socketio.on('getProducts')
def product_list(data):

    user = User.query.filter_by(mail=data['mail']).first()

    if(user):
        products = Product.query.filter_by(owner=user)
        productList = []
        for product in products:
            productList.append(
                {
                    "id": int(product.id),
                    "productName": product.productName,
                    "contains": int(product.contains),
                    "unit": product.unit,
                    "price": float(product.price),
                    "qty": int(product.qty)
                },
            )
        emit('getProducts',  {'data': productList, 'units': ["PCS", "KG"]})
    else:
        emit('getProducts', {'data': []})
