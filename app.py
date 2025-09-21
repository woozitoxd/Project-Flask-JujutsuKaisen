from flask import Flask, render_template, url_for
import os
from forocomunidad import comunidad_bp
from api.characters_api import characters_bp

app = Flask(__name__)



videos = [
    {
        "title": "Opening 1 - Kaikai Kitan",
        "description": "Primer opening de la serie",
        "url": "https://www.youtube.com/embed/1tk1pqwrOys"
    },
    {
        "title": "Opening 2 - 'Specialz'",
        "description": "Trailer Season 2",
        "url": "https://www.youtube.com/embed/5yb2N3pnztU?list=RD5yb2N3pnztU"
    }
]

@app.route("/")
def home():
    nav_items = [
    {"name": "Personajes", "href": "#character-section"},
    {"name": "Videos", "href": "#videos-section"},
    {"name": "Manga", "href": "#"}
]
    return render_template("index.html", videos=videos, nav_items=nav_items)

#Registramos los blueprints
app.register_blueprint(comunidad_bp, url_prefix="/forocomunidad")
app.register_blueprint(characters_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
