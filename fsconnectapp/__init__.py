from flask import Flask
from .main.routes import main
from .extensions import db


def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('C:\Akash Files\ShopifyAPp\Shopify Extension Application\config.ini')
    app.config['SECRET_KEY']='thisissecret' 
    # app.config.from_pyfile('/home/fsdev/python-instance/ShopifyExtensionApplication_backend/config.ini')
    app.config['SQLALCHEMY_DATABASE_URI']=app.config['MYSQL_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True, "pool_recycle": 300}
    db.init_app(app)
    app.register_blueprint(main)
    return app