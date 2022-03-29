from flask import jsonify
from repositories.user_repo import UserRepo
from repositories.book_repo import BookRepo

userRepo = UserRepo()
bookRepo = BookRepo()

def init():
    data = {"user_name":"admin","password":"123"}
    user = userRepo.create(data)
    data = {"name":"book1","user_id":user.id}
    user = bookRepo.create(data)
    return {}
