import operator
from datetime import timedelta

from flask import Blueprint, render_template

from management.routes import max_product_number
from models import Order, OrderItem
from .forms import ReportsRange

reports = Blueprint('reports', __name__)

title = "Report page"


@reports.route("/reports")
def all_reports():
    return render_template('reports.html', title=title)


@reports.route("/reports/by_date", methods=['GET', 'POST'])
def by_date():
    request_to_db = 0
    form = ReportsRange()
    filter_from = form.data_from.data
    filter_to = form.data_to.data + timedelta(days=1)
    orders = Order.query.join(OrderItem, OrderItem.order_id == Order.number).add_columns(Order.created_date,
                                                                                         OrderItem.product_price,
                                                                                         OrderItem.product_name,
                                                                                         OrderItem.order_id,
                                                                                         OrderItem.amount).filter(
        Order.created_date.between(filter_from, filter_to)).all()
    request_to_db += 1
    return render_template('reports_range.html', title=title, form=form, orders=orders, request_to_db=request_to_db)


@reports.route("/reports/top100")
def top():
    request_to_db = 0
    top_amount = {}
    list_of_elemetns = []
    for item in range(1, max_product_number + 1):
        product = f"Товар - {item}"
        request = OrderItem.query.filter_by(product_name=product).count()
        top_amount[f"Товар - {item}"] = request
        request_to_db += 1
    for key in range(1, len(top_amount)):
        product = f"Товар - {key}"
        item = max(top_amount.items(), key=operator.itemgetter(1))[0]
        items_from_db = Order.query.join(OrderItem, OrderItem.order_id == Order.number).add_columns(Order.created_date,
                                                                                                    OrderItem.product_price,
                                                                                                    OrderItem.product_name,
                                                                                                    OrderItem.order_id).filter_by(
            product_name=product).all()
        request_to_db += 1
        list_of_elemetns.extend(items_from_db)
        del top_amount[item]
    return render_template('reports_top.html', top_list=list_of_elemetns, title=title, request_to_db=request_to_db)
