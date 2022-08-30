from flask import Blueprint, request
from app.inventory.models import Product
from app.users.models import User
from flask_socketio import emit, send
from app import socketio, db
from app.error_codes import ErrorCodes

inventory = Blueprint('inventory', __name__)

clients = []


@socketio.on('getProducts')
def product_list(data):

    user = User.query.filter_by(mail=data['mail']).first()
    token = data['token']
    client = {
        "id": request.sid,
        "mail": data['mail'],
        "connections": 1
    }
    clients.append(client)

    if (user and user.token == token):
        products = Product.query.filter_by(owner=user)
        productList = []
        for product in products:
            productList.append(
                {
                    "id": int(product.product_id),
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


@socketio.on('addProduct')
def add_product(dataFromServer):
    status = False
    errorCode = ErrorCodes.noError
    data = "You don't have access to this route"
    user = User.query.filter_by(mail=dataFromServer['mail']).first()
    token = data['token']

    if (user and user.token == token):
        productExist = Product.query.filter_by(
            product_id=dataFromServer['id'], owner=user).first()
        if (not productExist):
            product = Product(
                product_id=int(dataFromServer['id']),
                productName=dataFromServer['productName'],
                contains=int(dataFromServer['contains']),
                price=float(dataFromServer['price']),
                unit=dataFromServer['unit'],
                owner=user
            )

            db.session.add(product)
            try:
                db.session.commit()
                status = True
                addedProduct = Product.query.get(product.id)
                data = {
                    "id": addedProduct.product_id,
                    "productName": addedProduct.productName,
                    "contains": addedProduct.contains,
                    "unit": addedProduct.unit,
                    "price": addedProduct.price,
                    "qty": addedProduct.qty
                }

            except Exception as e:
                status = False
                errorCode = ErrorCodes.sqlError
                data = str(e)
        else:
            status = False
            errorCode = ErrorCodes.productIdUniqueError
            data = "Product ID already exist"

    emit('addProduct', {"status": status,
         "errorCode": errorCode, "data": data})


@inventory.route('/delete_product', methods=['POST'])
def delete_product():
    status = False
    message = "You don't have access to this route"
    data = request.get_json()

    user = User.query.filter_by(mail=data['mail']).first()
    token = data['token']
    if (user and user.token == token):
        deleteProduct = Product.query.filter_by(
            owner=user, product_id=data['product_id']).first()
        if (deleteProduct):
            try:
                db.session.delete(deleteProduct)
                db.session.commit()
                status = True
                message = {
                    "id": deleteProduct.product_id,
                    "productName": deleteProduct.productName,
                    "contains": deleteProduct.contains,
                    "unit": deleteProduct.unit,
                    "price": deleteProduct.price,
                    "qty": deleteProduct.qty
                }
            except Exception as e:
                status = False
                message = str(e)
        else:
            status = False
            message = "Product already deleted or doesn't exist"
    to_client = {
        "status": status,
        "data": message
    }
    return to_client
