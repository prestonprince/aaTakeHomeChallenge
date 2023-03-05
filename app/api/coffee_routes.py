from flask import Blueprint, request
from app.models import Coffee, Post
from app.utils import validation_errors_to_error_messages
from sqlalchemy import desc


coffee_routes = Blueprint('coffee', __name__)


@coffee_routes.route('/ping')
def ping():
    return { 'status': 'good' }


@coffee_routes.route('')
def all_coffee():
    """
    Returns all coffees ordered by name in desc or asc
    """
    order = request.args['order']
    all_coffees = Coffee.query.order_by(Coffee.name).all() if order == 'asc' else Coffee.query.order_by(desc(Coffee.name)).all()

    coffees = [coffee.to_dict() for coffee in all_coffees]
    print(coffees)
    return {'coffee': coffees}
