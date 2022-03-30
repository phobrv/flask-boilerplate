from crypt import methods
from flask import Blueprint
from controller import User,Init

route = Blueprint('route', __name__)

@route.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    return User.get(user_id)

@route.route("/users",methods=["GET"])
def get_list_user():
    return User.get_list_user()

@route.route("/user/<int:user_id>",methods=["DELETE"])
def del_user(user_id):
    return User.del_user(user_id)

@route.route("/init", methods=["GET"])
def init():
    return Init.init()