from flask import Blueprint, request
from app.inventory.models import Product
from app.users.models import User

inventory = Blueprint('inventory', __name__)


@inventory.route('/inventory', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(mail=data['mail']).first()
    if user:
        response = []
        products = Product.query.filter_by(owner=user)
        for product in product:
            response.append({
                "status": True,
                "data": {"id": product.id,
                         "productName": product.productName,
                         "contains": product.contains,
                         "unit": product.unit,
                         "price": product.price,
                         "qty": product.qty}
            })
    else:
        response = {"status": False, "data": {
            "message": "You don't have access to this page"}}
    return response
