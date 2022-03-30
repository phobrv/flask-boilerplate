from flask import jsonify
from repositories.user_repo import UserRepo
from repositories.book_repo import BookRepo
import randomname

userRepo = UserRepo()
bookRepo = BookRepo()

def init():
    username = randomname.get_name()
    data = {"user_name":username,"password":"123"}
    user = userRepo.create(data)
    book = randomname.get_name()
    data = {"name":book,"user_id":user.id}
    user = bookRepo.create(data)
    return {}
