from flask import jsonify
from repositories.user_repo import UserRepo

userRepo = UserRepo()


def get(id):
    user = userRepo.get(id)
    return jsonify(user.serialize)