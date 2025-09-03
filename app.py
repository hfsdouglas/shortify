import os
from flask import Flask
from app.database.db import db

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "app", "database", "shortify.db")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"

    db.init_app(app)

    from app.routes.api import api
    api(app)

    from app.routes.web import web
    web(app)

    return app

app = create_app()

if __name__ == "__main__":
  app.run(debug=True)