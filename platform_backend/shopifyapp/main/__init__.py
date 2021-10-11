from flask import Blueprint
from flask_marshmallow import Marshmallow

main = Blueprint('main', __name__)
ma = Marshmallow(main)