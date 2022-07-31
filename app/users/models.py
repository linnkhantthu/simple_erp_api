from app import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(60))
    lastName = db.Column(db.String(60))
    mail = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def validate_mail(self):
        user = User.query.filter_by(mail=self.mail).first()
        if(user):
            raise Exception("User already exists.")
