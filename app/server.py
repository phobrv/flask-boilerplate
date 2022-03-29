from flask import Flask
from flask_cors import CORS
import config
from model import db
from routes import app

server = Flask(__name__)
server.debug = config.DEBUG

server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(server)
db.app = server

CORS(
    server,
    resources={r"/*": {"origins": "*"}},
    headers=["Content-Type", "X-Requested-With", "Authorization"],
)
server.register_blueprint(app)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
