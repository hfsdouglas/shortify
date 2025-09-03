import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = os.path.join(app.root_path + '/database', 'shortify.db')

    from .database import db
    db.init_app(app)

    from .routes.api import api
    api(app)

    from .routes.web import web
    web(app)

    return app