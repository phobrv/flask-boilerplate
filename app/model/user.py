from . import db
from datetime import datetime
import bcrypt

salt = bcrypt.gensalt()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(50), nullable=True)
    update_at = db.Column(db.String(50), nullable=True)
    user_name = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(100), nullable=True)  # hashed
    books = db.relationship("Book", backref="users",  lazy="subquery")

    def __init__(self):
        self.created_at = str(datetime.now())
        self.update_at = str(datetime.now())

    def init(self, setter:dict):
        for k, v in setter.items():
            if k=="password":
                setattr(self, k, self.hash_password(v))
            else:
                setattr(self, k, v)
        self.created_at = str(datetime.now())
        self.update_at = str(datetime.now())

    def hash_password(self, input_passwd):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(input_passwd.encode("utf-8"), salt)
        return hashed.decode("utf-8")
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'user_name':self.user_name,
            'books': [book.serialize for book in self.books if book is not None],
        }
