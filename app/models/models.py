from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
database = SQLAlchemy()


# Modelo de usuario
class User(UserMixin, database.Model):
    __tablename__ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    password = database.Column(database.String(100), nullable=False)
    correo = database.Column(database.String(50), nullable=False)

    # Relación con comentarios
    comentarios = database.relationship('Comentario', backref='usuario', lazy=True)


# Modelo de comentario
class Comentario(database.Model):
    __tablename__ = 'comentarios'

    id = database.Column(database.Integer, primary_key=True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False)
    comentario = database.Column(database.String(200), nullable=False)
