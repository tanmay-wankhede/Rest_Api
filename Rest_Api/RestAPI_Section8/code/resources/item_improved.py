from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item_model import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('store_id', type=int, required=True, help="every item need a store id")
   
    #@jwt_required()                            #authenticate before the get request
    def get(self,name):                              # here we define our own get function which process get request
        item = ItemModel.find_by_name(name)
        if item:
            return item.json() 
        return {'message':'item not found'},404
    
    

    def post(self,name):
        if ItemModel.find_by_name(name): #if name is already in it and they try to post it again
            return {'message':f"an item name {name} already exists."}
        
        data = Item.parser.parse_args()
        #data  = request.get_json()     #.get_json(force = True) means that it does not look in content type header
        item = ItemModel(name,data['price'],data['store_id']) 
        try:               
            item.save_to_db()
        except:
            return {'message':'an error occured inserting item'},500 #means not inserters fault , internal server error                  
        return item.json(), 201   #201 is craeted code

       
    #@jwt_required()   this will also enable authentication in delete also
    def delete(self,name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()

        # return {'message':'item deleted'}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'item deleted'}
        
    def put(self,name):
        #parser = reqparse.RequestParser() #view sec 4 last secnd video, try to do this in other requests to
        #parser.add_argument('price',type = float, required = True,help = 'this field cannot be left blank!')
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel( name, data['price'])
        
        if item is None:
            # try:
            #     updated_item.insert()
            # except:
            #      return {'message':"an error occured inserting the item"},500
            item = ItemModel(name, data['price'],data['store_id'])        
        else:
            # try:
            #     updated_item.updtae()
            # except:
            #     return {'message':'an error occured updating the item'},500
            item.price = data['price']

        item.save_to_db()    
        return item.json() 

    
                

class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result = cursor.execute(query) # now this is s iterable because not other argument
        
        # items = []

        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})
        
        # #not connection.commit because we didnt save anything
        # connection.close()
        
        # return {'items':items}

        return {'items':[item.json() for item in ItemModel.query.all()]}  # ItemModel.query.all() return all the items