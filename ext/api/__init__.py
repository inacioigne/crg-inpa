from flask import Blueprint
from .api import bp_api

def init_app(app):
    app.register_blueprint(bp_api)