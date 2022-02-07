from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app,authenticate,identity)

#temp data

items = []

class Item(Resource):
    @jwt_required() #decorator dat je moet geauthenticeerd zijn voordat je een get kunt doen
    def get(self, name):
        #for item in items:
            #if item['name'] == name:
                #return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        #return {'message':"Sorry, couldn't find an item with the name "+name}, 404
        return {'item': item}, 200 if item is not None else 404

    def post(self, name):

        if next(filter(lambda x: x['name'] == name, items), None) is not None:    #unique name
            return {'message', "An item with name "+name+" already exists."},400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items #items variable is outer variable
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item has been deleted!'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be left blank!'
        )
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)

        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') # dit replaces de decorator @app.route('/student/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000, debug=True)
