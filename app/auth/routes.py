from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.models import User
from app import bcrypt, database as db

# Definición del Blueprint
loginRegister = Blueprint("auth", __name__)

# -----------------------------
# Ruta: /auth/login
# -----------------------------
@loginRegister.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Buscar usuario por nombre o correo
        user = User.query.filter(
            (User.nombre == username) | (User.correo == username)
        ).first()

        if user and bcrypt.check_password_hash(user.password, password): #Busca el usuario y verifica la contraseña
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("main.home"))  # Redirige a la vista principal
        else:
            flash("Credenciales inválidas", "danger")

    return render_template("index.html")


# -----------------------------
# Ruta: /auth/register
# -----------------------------
@loginRegister.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")

        # Crear usuario y guardar en la base de datos
        nuevo_usuario = User(nombre=username, correo=email, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Registro exitoso. Ya puedes iniciar sesión.", "success")
        return redirect(url_for("auth.login"))

    return render_template("index.html")


# -----------------------------
# Ruta: /auth/logout
# -----------------------------
@loginRegister.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión.", "info")
    return redirect(url_for("auth.login"))


