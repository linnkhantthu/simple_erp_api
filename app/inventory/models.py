from app import db


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    productName = db.Column(db.String(60), nullable=False)
    contains = db.Column(db.String(60), nullable=False)
    unit = db.Column(db.String(150), unique=True, nullable=False)
    price = db.Column(db.String(150), nullable=False)
    qty = db.Column(db.String(150), default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Product {self.productName}>"
