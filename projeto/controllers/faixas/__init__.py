from flask import Blueprint

faixas_bp = Blueprint("faixas", __name__, template_folder="templates", static_folder='static')

from controllers.faixas import routes