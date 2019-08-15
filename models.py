import random

from db import db


class Order(db.Model):
    __tablename__ = 'orders'
    number = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    purchase = db.relationship('OrderItem', backref=db.backref('purchase'), lazy=True)

    def __init__(self, number, created_date):
        self.number = number
        self.created_date = created_date


class OrderItem(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=random.randint(0, 10))
    order_id = db.Column(db.Integer, db.ForeignKey(Order.number), nullable=False)

    def __init__(self, product_name, product_price, amount, order_id):
        self.product_name = product_name
        self.product_price = product_price
        self.amount = amount
        self.order_id = order_id
