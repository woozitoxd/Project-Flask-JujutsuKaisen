from flask import Blueprint

comunidad_bp = Blueprint("comunidad", __name__, template_folder="templates")

from . import routes
