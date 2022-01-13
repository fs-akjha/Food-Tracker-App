from flask import Blueprint, config,Flask
from flask_marshmallow import Marshmallow
from flask_ngrok import run_with_ngrok



main = Blueprint('main', __name__)
ma = Marshmallow(main)

app = Flask(__name__)

app.config.from_pyfile('C:\Akash Files\FleetStudioCo\FSConnectBackendcode\config.ini')