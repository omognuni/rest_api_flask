from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []
# every resources Class
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        
        return {'item': None}, 404
    
    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201 # created status code
#app.route()
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/<string:name>

app.run(port=5000)

