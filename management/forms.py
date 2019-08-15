from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class Orders(FlaskForm):
    orders = IntegerField("*Number of orders", validators=[DataRequired()])
    submit = SubmitField('Order')
