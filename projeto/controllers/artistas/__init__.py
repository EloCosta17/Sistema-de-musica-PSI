from flask import Blueprint

artistas_bp = Blueprint("artistas", __name__, template_folder="templates", static_folder='static')

from controllers.artistas import routes