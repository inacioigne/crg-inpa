from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager
#from crg.ext.cli.create import create

engine = create_engine('mariadb+mariadbconnector://admin:8486@localhost/crg')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
login_manager = LoginManager()


def init_app(app):

    @app.before_first_request
    def initializeDatabase():
        from .models import User
        import crg.ext.db.models
        #from .user_model import Usuarios
        #import crg.ext.db.coleta_model

        Base.metadata.create_all(bind=engine)
        login_manager.init_app(app)

        @login_manager.user_loader
        def user_loader(id):
            return session.query(User).filter_by(id=id).first()

        @login_manager.request_loader
        def request_loader(request):
            username = request.form.get('username')
            user = session.query(User).filter_by(username=username).first()
            return user if user else None

        #create(Usuarios, Colecao)

    @app.teardown_request
    def shutdown_session(exception=None):
        session.remove()