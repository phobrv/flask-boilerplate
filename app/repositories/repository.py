from abc import ABC, abstractmethod
from model import db
from loguru import logger


class Repository(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def all(self):
        obj = db.session.query(self.model).all()
        db.session.remove()
        return obj

    @abstractmethod
    def get(self, id):
        obj = db.session.query(self.model).filter_by(id=id).first()
        db.session.remove()
        return obj

    @abstractmethod
    def filter(self,dictionaries,scope):
        query = db.session.query(self.model)
        for k , v in dictionaries.items():
            query = query.filter(getattr(self.model, k) == v) 
        if scope == 'first':
            obj = query.first()
        else:
            obj = query.all()
        db.session.remove()
        return obj

    @abstractmethod
    def create(self,data):
        obj = self.model()
        obj.init(data)
        db.session.add(obj)
        db.session.commit()
        return obj

    @abstractmethod
    def update(self,dictionaries,id):
        query = db.session.query(self.model).filter_by(id=id)
        for k , v in dictionaries.items():
            query = query.update({k: v})
        db.session.commit()
        return {}


    @abstractmethod
    def delete(self,id):
        obj = self.get(id)
        db.session.delete(obj)
        db.session.commit()
        return {}