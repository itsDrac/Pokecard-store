from app.extinsions import db, login_manager
from app.user.models import User

class Type(db.Document):
    name = db.StringField(max_length=30)

class Data(db.EmbeddedDocument):
    types = db.ListField(db.ReferenceField(Type), min_entries = 1)
    species = db.StringField(max_length=30)
    height = db.StringField(max_length=20)
    weight = db.StringField(max_length=20)
    abilities = db.ListField(db.StringField(max_length=30), min_entries = 1)

class Stats(db.EmbeddedDocument):
    hp = db.IntField(min_value=1, max_value=9, required=True)
    attack = db.IntField(min_value=1, max_value=9, required=True)
    defense = db.IntField(min_value=1, max_value=9, required=True)
    speed = db.IntField(min_value=1, max_value=9, required=True)

class Product(db.Document):
    name = db.StringField(required=True)
    img = db.URLField(required=True, unique=True)
    gen = db.IntField(min_value=1, max_value=9, required=True)
    data = db.EmbeddedDocumentField(Data)
    stats = db.EmbeddedDocumentField(Stats)
