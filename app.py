from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from auth import authenticate, identity
from api.product import Product, ProductList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'test'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Product, '/product')
api.add_resource(ProductList, '/product/list')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=2000, debug=True)
