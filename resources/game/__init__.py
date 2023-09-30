from flask_smorest import Blueprint

bp = Blueprint('game', __name__, url_prefix='/Game')

from . import routes