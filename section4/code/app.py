from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
# JWT (json web token)
app.secret_key = 'melbong'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []
# every resources Class


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @jwt_required()
    def get(self, name):
        # next: first item found by filter / no item, return None
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)

        if item is not None:
            # bad request(invalid name)
            return {'message': f'An item with {name} already exists.'}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # created status code

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)

        else:
            item.update(data)

        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


# app.route()
# http://127.0.0.1:5000/item/<string:name>
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
