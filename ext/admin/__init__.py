from .admin import admin

def init_app(app):
    admin.init_app(app)