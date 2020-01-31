from flask import Flask
from flask_restful import Api
from resources.item import Item, ItemList
from resources.store import Store, StoreList, RemoveItems
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)

db.init_app(app)

#funzione di Flask che crea le tabelle nel database prima della prima request (solo se non esistono gia'
@app.before_first_request
def create_tables():
    db.create_all()



# @app.route('/v1/auth', methods=['POST'])
# def aut():
  #   username = request.args.get('username', '', type=str)
    # password = request.args.get('password', '', type=str)
    # return authenticate(username, password)




@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RemoveItems, '/store/<int:id>')

if __name__ == '__main__':
    app.run()
