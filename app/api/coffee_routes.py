from flask import Blueprint, request
from app.models import db, Coffee, Post
from app.forms import CreateCoffee
from app.utils import validation_errors_to_error_messages, normalize
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
    order = 'asc' if len(request.args) == 0 else request.args['order']
    all_coffees = Coffee.query.order_by(Coffee.name).all() if order == 'asc' else Coffee.query.order_by(desc(Coffee.name)).all()
    coffees = [ coffee.to_dict() for coffee in all_coffees ]
    return { 'coffee': coffees }


@coffee_routes.route('/<int:id>')
def get_coffee(id):
    """
    Query for and return single coffee by id
    """
    #todo 
    # error handling

    coffee = Coffee.query.get(id).to_dict()

    return { "coffee": coffee }


@coffee_routes.route('/create/', methods=['POST'])
def create_coffee():
    """
    Creates new coffee
    """
    form = CreateCoffee()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        name = data['name'].capitalize()
        new_coffee = Coffee(
            name=name,
            year=data['year'],
            caffeine_content=data['caffeine']
        )
        
        db.session.add(new_coffee)
        db.session.commit()
        return new_coffee.to_dict(), 201
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401


@coffee_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_coffee(id):
    """
    Query for and delete coffee by id
    returns success message if deleted
    returns error message if unsuccessful
    """
    coffee = Coffee.query.get(id)

    if not coffee:
        return {'errors': 'Coffee not found'}
    
    coffee_posts = coffee.posts
    if len(coffee_posts) > 0:
        for post in coffee_posts:
            db.session.delete(report)
            db.session.commit()

    db.session.delete(coffee)
    db.session.commit()
    return {'message': 'coffee successfully deleted'}
