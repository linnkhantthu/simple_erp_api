from app import create_app, socketio
from flask_socketio import emit

from app.inventory.models import Product
from app.users.models import User

app = create_app()


@socketio.on('connect')
def test_connect():
    dummyProductList = [
        {
            "id": 1,
            "productName": "Cow Hat",
            "contains": 100,
            "unit": "PCS",
            "price": 2500.0,
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
    emit('getProducts',  {'data': dummyProductList})


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    socketio.run(app=app, host='0.0.0.0', debug=True)
