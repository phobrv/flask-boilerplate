from flask import Flask
from flask_cors import CORS
import config
from model import db


app = Flask(__name__)
app.debug = config.DEBUG

app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(app)
db.app = app

CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    headers=["Content-Type", "X-Requested-With", "Authorization"],
)


from controller import User,Init


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    return User.get(user_id)

@app.route("/init", methods=["GET"])
def init():
    return Init.init()


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
