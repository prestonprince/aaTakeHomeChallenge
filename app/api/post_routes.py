from flask import Blueprint, request
from app.models import db, Post
from app.utils import validation_errors_to_error_messages
from sqlalchemy import desc


post_routes = Blueprint('posts', __name__)


@post_routes.route('/ping')
def ping():
    return { 'status': 'good' }


@post_routes.route('')
def get_all_posts():
    """
    get all posts and order them by asc or desc date
    """
    pass #todo


@post_routes.route('/<int:id>')
def get_one_post(id):
    """
    query for and return a single post by id
    """
    post = Post.query.get(id)

    if not post:
        return {'error': 'Post not found'}, 404

    return { 'post': post.to_dict() }


@post_routes.route('/<int:id>', methods=['DELETE'])
def delete_post(id):
    """
    Query for and delete post by id
    """
    post = Post.query.get(id)
    if not post:
        return {'error': 'Post not found'}, 404

    db.session.delete(post)
    db.session.commit()
    return {'message': 'coffee successfully deleted'}
