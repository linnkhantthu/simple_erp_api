from ast import Expression
from flask import Blueprint, jsonify, request
from app.inventory.models import Product
from app.users.models import User
from app import db

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


@inventory.route('/addProduct', methods=['POST'])
def addProduct():
    status = False
    new_data = {
        "message": "You don't have access to this page",
    }
    data = request.get_json()
    product_data = data['product']
    user = User.query.filter_by(mail=data['mail']).first()
    if user:
        product = Product.query.filter_by(
            owner=user, id=product_data['id']).first()
        if product:
            status = False
            new_data = {
                "message": "This product ID is already exist.",
            }
        else:
            product = Product(
                id=int(product_data['id']),
                productName=product_data['productName'],
                contains=int(product_data['contains']),
                price=float(product_data['price']),
                unit=product_data['unit'],
                owner=user
            )
            db.session.add(product)
            try:
                db.session.commit()
                product = Product.query.filter_by(
                    owner=user, id=product_data['id']).first()
                if product:
                    status = True
                    new_data = {"id": int(product.id),
                                "productName": product.productName,
                                "contains": int(product.contains),
                                "unit": product.unit,
                                "price": float(product.price),
                                "qty": int(product.qty)}

                else:
                    status = False
                    new_data = {
                        "message": "Something went wrong while inserting data to the database",
                    }
            except Exception as e:
                print(e)
                status = False
                new_data = {
                    "message": str(e),
                }
    else:
        status = False
        new_data = {
            "message": "You don't have access to this page",
        }
    response = {
        "status": status,
        "data": new_data,
    }
    return response
