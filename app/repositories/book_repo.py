from model.book import Book
from repositories.repository import Repository


class BookRepo(Repository):
    def __init__(self):
        super().__init__(Book)

    def get(self, id):
        return super().get(id)

    def all(self):
        return super().all()

    def create(self, data):
        return super().create(data)

    def delete(self, id):
        return super().delete(id)

    def filter(self, dictionaries, scope):
        return super().filter(dictionaries, scope)
        
    def update(self, dictionaries, id):
        return super().update(dictionaries, id)
