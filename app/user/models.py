from app.extinsions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    _id = db.StringField()
    name = db.StringField()
    email = db.EmailField(domain_whitelist=['com'], unique = True)
    password = db.StringField()

    def __repr__(self):
        return f"User[id : '{self._id}', Name : '{self.name}', Email : '{self.email}']"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
