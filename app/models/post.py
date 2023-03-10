from .db import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffee.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    coffee = db.relationship("Coffee", back_populates='posts')
    
    def to_dict_base(self):
        return {
            "id": self.id,
            "title": self.title,
            "coffee_id": self.coffee_id,
            "text": self.text,
            "rating": self.rating,
            "created_at": self.created_at,
        }
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "coffee_id": self.coffee_id,
            "text": self.text,
            "rating": self.rating,
            "created_at": self.created_at,
            "coffee": self.coffee.to_dict()
        }
