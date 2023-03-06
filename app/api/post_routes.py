from flask import Blueprint, request
from app.models import db, Post
from app.utils import validation_errors_to_error_messages
from sqlalchemy import desc


post_routes = Blueprint('posts', __name__)


@post_routes.route('/ping')
def ping():
    return { 'status': 'good' }
