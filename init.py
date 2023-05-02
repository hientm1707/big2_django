import types
import logging

import b2_bookstore
import base

from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
logging.basicConfig(level=logging.INFO)

blueprints = [
    base.controllers.auth_routes.auth,
    b2_bookstore.controllers.bookstore_routes.b2_bookstore
]


def create_app():
    def register_blueprints(self, blueprints):
        for bp in blueprints:
            logging.info(f'REGISTERD BLUEPRINT: {bp.name}')
            self.register_blueprint(bp)

    def create_login_manager():
        login_manager = LoginManager()
        login_manager.session_protection = 'strong'
        login_manager.login_message_category = 'info'
        return login_manager

    webapp = Flask(__name__)
    webapp.config.from_object('config')
    webapp.register_blueprints = types.MethodType(register_blueprints, webapp)
    webapp.register_blueprints(blueprints)
    create_login_manager().init_app(webapp)
    bcrypt.init_app(webapp)
    db.init_app(webapp)
    return webapp
