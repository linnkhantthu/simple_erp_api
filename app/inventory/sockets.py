from flask import Blueprint

ws = Blueprint(r'ws', __name__)


@ws.route("/product_list")
def products(json):
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
    # data = request.get_json()
    data = json
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
        # return send(response)
    else:
        response = {"status": False, "data": {
            "message": "You don't have access to this page"}}
        # return send(response)
    return send(response)
