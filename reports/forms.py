from datetime import date, datetime

from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired


class ReportsRange(FlaskForm):
    data_from = DateField("*From date", validators=[DataRequired()], default=datetime(year=2018, month=1, day=1))
    data_to = DateField("*To date", validators=[DataRequired()], default=date.today)
    submit = SubmitField('Show')
