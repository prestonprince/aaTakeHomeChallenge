from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Coffee


def is_name_length_valid(form, field):
    # checks if length of name is 50 characters or less
    name = field.data
    if len(name) > 50:
        raise ValidationError('Name must be 50 characters or less')


def is_valid_year(form, field):
    # checks if year is valid
    # year is valid if len of year is 4 or less and if not greater than current year
    year = field.data

    if year < 1 or year > 2023:
        raise ValidationError('Year not valid')


class CreateCoffee(FlaskForm):
    name = StringField('name', validators=[DataRequired(), is_name_length_valid])
    year = IntegerField('year', validators=[DataRequired(), is_valid_year])
    caffeine = IntegerField('caffeine', validators=[DataRequired()])
