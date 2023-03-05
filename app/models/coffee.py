from .db import db


class Coffee(db.Model):
    __tablename__ = 'coffee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    caffeine_content = db.Column(db.Integer, nullable=False)
    caffeine_percentage = db.Column(db.Numeric(precision=4, scale=2))

    @property
    def _caffeine_percentage(self):
        return self.caffeine_percentage
    
    @_caffeine_percentage.setter
    def _caffeine_percentage(self, percentage):
        self.caffeine_percentage = percentage
