from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
     def get(self, name):
         #improving by lambda func
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
     
     def post(self, name):
         if next(filter(lambda x: x['name'] == name, items), None) is not None:
             return {'message': "An item with name '{}' already exists.".format(name)}, 400
             
         
         data = request.get_json() #force=True silent= True
         item = {'name': name, 'price':  data['price']}
         items.append(item)
         return item, 201 #created code
#202 accepted code
     
     
class ItemList(Resource):
    def get(self):
        return {'items': items}
    
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)