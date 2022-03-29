import os, logging

DEBUG = True
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT", "5000"))

POSTGRES = {
    "user": os.getenv("POSTGRES_USER", "flask"),
    "pw": os.getenv("POSTGRES_PW", "password"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "db": os.getenv("POSTGRES_DB", "flask_db"),
}
DB_URI = "postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
