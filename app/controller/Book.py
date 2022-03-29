from flask import jsonify
from repositories.book_repo import BookRepo

bookRepo = BookRepo()


def get(id):
    user = bookRepo.get(id)
    return jsonify(user)
