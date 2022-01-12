from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('C:\Akash Files\ShopifyAPp\Shopify Extension Application\config.ini')
# app.config.from_pyfile('/home/fsdev/python-instance/ShopifyExtensionApplication_backend/config.ini')