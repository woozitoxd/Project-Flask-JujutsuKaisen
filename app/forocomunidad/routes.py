from flask import Blueprint, render_template, request, redirect, url_for

#Simulación de una base de datos en memoria de comentarios

comunidad_bp = Blueprint("comunidad", __name__, template_folder="templates")

comentarios = [] # Lista para almacenar comentarios

@comunidad_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        autor = request.form.get("autor")
        comentario = request.form.get("comentario")
        if autor and comentario:
            comentarios.append({"autor": autor, "comentario": comentario})
        return redirect(url_for("comunidad.index"))  # nombre del blueprint, no url_prefix
    
    return render_template("comunidad/index.html", comentarios=comentarios)