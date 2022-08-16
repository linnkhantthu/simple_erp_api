from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    productName = db.Column(db.String(60), nullable=False)
    contains = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Product {self.productName}>"


class Unit(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    unit = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Unit {self.unit}>"
