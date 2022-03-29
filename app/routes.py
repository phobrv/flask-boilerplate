from flask import Blueprint
from controller import User,Init

app = Blueprint('route', __name__, template_folder='app')

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    return User.get(user_id)

@app.route("/init", methods=["GET"])
def init():
    return Init.init()