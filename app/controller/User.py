from flask import jsonify
from repositories.user_repo import UserRepo

userRepo = UserRepo()


def get(id):
    user = userRepo.get(id)
    return jsonify(user.serialize)
def get_list_user():
    users = userRepo.all()
    return jsonify([i.serialize for i in users])
def del_user(user_id):
    return userRepo.delete(user_id)