#seperating items and stores con items cannot be within stores
#items and stores are no longer goini to be list but dictnory

# stores = {}
# items = {}


#    stores = [
#       {
#            "name": "My Store",
#            "items": [
#                {
#                    "name": "Chair",
#                    "price": 15.99
#                }
#            ]
#        }
#    ]

#create first endpoint

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()      #