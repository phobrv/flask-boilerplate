from . import db
from datetime import datetime


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(50), nullable=True)
    update_at = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="books", lazy="subquery")

    def __init__(self):
        self.created_at = str(datetime.now())
        self.update_at = str(datetime.now())

    def init(self, setter:dict):
        for k, v in setter.items():
            setattr(self, k, v)
        self.created_at = str(datetime.now())
        self.update_at = str(datetime.now())
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name':self.name
        }