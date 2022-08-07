from app import create_app, socketio
from flask_socketio import emit

from app.inventory.models import Product
from app.users.models import User

app = create_app()
socketio.async_mode = True


@socketio.on('getProducts')
def product_list(data):

    dummyProductList = [
        {
            "id": 11,
            "productName": "Cow Hat",
            "contains": 100,
            "unit": "PCS",
            "price": 3500.0,
            "qty": 150
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

        emit('getProducts',  {'data': productList})
    else:
        emit('getProducts', {'data': []})


if __name__ == "__main__":

    socketio.run(app=app, host='0.0.0.0', debug=True)
