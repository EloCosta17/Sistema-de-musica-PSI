from flask import Blueprint

albuns_bp = Blueprint("albuns", __name__, template_folder="templates", static_folder='static')

from controllers.albuns import routes