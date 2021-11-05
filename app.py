from flask import Flask
from crg.ext import site
from crg.ext import admin
from crg.ext import db
from crg.ext import api
from flask_cors import CORS
from crg.ext.email import mail

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    site.init_app(app)
    admin.init_app(app)
    api.init_app(app)
    mail.init_app(app)
    CORS(app)
    cors = CORS(app, resources={
        r"/*" : {
            "origins": "*"
        }
    })


    return app
