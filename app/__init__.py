import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .models.models import User, Comentario, database
# Inicializar extensiones

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'supersecretkey'
    
    
    # Inicializar extensiones
    database.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    # Crear tablas
    with app.app_context():
        database.create_all()

    # Configurar login_manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar blueprints
    from app.forocomunidad.routes import comunidad_bp
    from app.api.characters_api import characters_bp
    from app.auth.routes import loginRegister
    from app.main.routes import main_bp

    app.register_blueprint(comunidad_bp, url_prefix="/forocomunidad")
    app.register_blueprint(characters_bp, url_prefix="/api")
    app.register_blueprint(loginRegister, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/")

    return app
