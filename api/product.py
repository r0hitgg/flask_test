from flask_restful import Resource, reqparse
from models.product import ProductModel


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="Name field cannot be left blank!"
                        )

    def get(self):
        data = Product.parser.parse_args()
        product = ProductModel.get_by_name(data.get('name'))
        if product:
            return product.json(), 200
        return {'message': 'Product not found'}, 404

    def post(self):
        Product.parser.add_argument('price',
                                    type=float,
                                    required=True,
                                    help="Price field cannot be left blank!"
                                    )
        data = Product.parser.parse_args()
        if ProductModel.get_by_name(data.get('name')):
            return {'message': "An Product with name '{}' already exists.".format(data.get('name'))}, 400

        product = ProductModel(**data)

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the Product."}, 500

        return product.json(), 200

    def delete(self):
        data = Product.parser.parse_args()
        product = ProductModel.get_by_name(data.get('name'))
        if product:
            product.delete_from_db()
            return {'message': 'Product deleted.'}
        return {'message': 'Product not found.'}, 404

    def put(self):
        Product.parser.add_argument('price',
                                    type=float,
                                    required=True,
                                    help="Price field cannot be left blank!"
                                    )
        data = Product.parser.parse_args()
        product = ProductModel.get_by_name(data.get('name'))
        if product:
            product.price = data.get('price')
        else:
            product = ProductModel(**data)

        product.save_to_db()

        return product.json(), 200


class ProductList(Resource):

    def get(self):
        return {'products': list(map(lambda x: x.json(), ProductModel.query.all()))}, 200
