import unittest
import json
from app import app
from db import db


class ProductTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.init_app(app)
        # self.db = db.get_db()

    def test_successful_product_create(self):
        payload = json.dumps({
            "name": "Product 1",
            "price": 500
        })

        response = self.app.post('/product', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(str, type(response.json['name']))
        self.assertEqual(200, response.status_code)

    def test_successful_product_get(self):
        payload = json.dumps({
            "name": "Product 1",
            "price": 500
        })

        response = self.app.get('/product', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['name']))
        self.assertEqual(200, response.status_code)

    def test_successful_product_put(self):
        payload = json.dumps({
            "name": "Product 1",
            "price": 800
        })

        response = self.app.put('/product', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(str, type(response.json['name']))
        self.assertEqual(800, response.json['price'])
        self.assertEqual(200, response.status_code)
