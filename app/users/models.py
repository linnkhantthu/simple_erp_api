from app import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(60), nullable=False)
    lastName = db.Column(db.String(60), nullable=False)
    mail = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    product = db.relationship('Product', backref='owner', lazy=True)

    def __repr__(self):
        return f"<User {self.mail}>"
