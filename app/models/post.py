from .db import db
from sqlalchemy.sql import func


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffee.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Numeric(precision=2, scale=1), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
