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
    unit = db.relationship('PurchaseVoucherItem', backref='product', lazy=True)

    def __repr__(self):
        return f"<Product {self.productName}>"


class Unit(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    unit = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Unit {self.unit}>"


class PurchaseVoucher(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    voucher_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0)
    purchasevoucheritem = db.relationship(
        'PurchaseVoucherItem', backref='voucher', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<PurchaseVoucher {self.voucher_id}>"


class PurchaseVoucherItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    purchase_voucher_id = db.Column(
        db.Integer, db.ForeignKey('purchasevoucher.id'), nullable=False)
    final_price = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<PurchaseVoucherItem {self.voucher_id}>"
