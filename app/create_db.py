from model import db
from app import server
with server.app_context():
    db.create_all()
