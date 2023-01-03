from db import db
from models.item import ItemModel


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    item = db.relationship("ItemModel", back_populates = "store", lazy = "dynamic")
    tags = db.relationship("TagModel", back_populates = "store", lazy = "dynamic")