import random
from datetime import datetime

from flask import Blueprint
from flask import render_template, flash
from sqlalchemy import func

from db import db
from forms import Orders
from models import Order, OrderItem

management = Blueprint('management', __name__)

title = "Management page"
max_product_number = 5


def set_time(number):
    default_time = 1514790000
    created_time = default_time + number * 60 * 60
    return datetime.fromtimestamp(created_time).strftime("%d.%m.%Y, %I:%M:%S")


@management.route("/", methods=['GET', 'POST'])
def home_page():
    form = Orders()
    if form.validate_on_submit():
        qty = form.orders.data
        for order in range(qty):
            qry = db.session.query(func.max(Order.number)).first()
            if qry[0] is None:
                id = 1
            else:
                id = qry[0] + 1
            created_date = set_time(id)
            order = Order(number=id, created_date=created_date)
            db.session.add(order)
            db.session.commit()
            for item in range(1, (random.randint(1, max_product_number) + 1)):
                prodcut_name = f"Товар - {item}"
                order_id = id
                product_price = random.randint(100, 9999)
                amount = random.randint(1, 10)
                order_item = OrderItem(
                    product_name=prodcut_name,
                    order_id=order_id,
                    product_price=product_price,
                    amount=amount
                )
                db.session.add(order_item)
                db.session.commit()
        flash(f'{qty} orders successfully created', 'success')

    return render_template('home.html', form=form, title=title)
