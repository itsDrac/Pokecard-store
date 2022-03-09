from flask import Blueprint

prod_bp = Blueprint('prod_bp', __name__,
                 template_folder='templates',
                 static_folder='static')

from . import routes
