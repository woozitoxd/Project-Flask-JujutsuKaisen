from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__, url_prefix="/")

@main_bp.route("/")
def home():
    videos = [
        {"title": "Opening 1 - Kaikai Kitan", "description": "Primer opening de la serie", "url": "https://www.youtube.com/embed/1tk1pqwrOys"},
        {"title": "Opening 2 - 'Specialz'", "description": "Trailer Season 2", "url": "https://www.youtube.com/embed/5yb2N3pnztU?list=RD5yb2N3pnztU"},
    ]
    nav_items = [
        {"name": "Personajes", "href": "#character-section"},
        {"name": "Videos", "href": "#videos-section"},
        {"name": "Manga", "href": "#"},
    ]
    return render_template("index.html", videos=videos, nav_items=nav_items)
