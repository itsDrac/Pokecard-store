from app.extinsions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.objects.get(pk=user_id)

class Cart(db.EmbeddedDocument):
    product = db.ReferenceField("Product", required = True)
    quntity = db.IntField(min_value=1, required=True, default=1)

class User(db.Document, UserMixin):
    name = db.StringField()
    email = db.EmailField(domain_whitelist=['com'], unique = True)
    password = db.StringField()
    cart = db.EmbeddedDocumentListField(Cart)

    def __repr__(self):
        return f"User[Name : '{self.name}', Email : '{self.email}', Cart: '{self.cart}']"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
