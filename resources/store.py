from flask_restful import Resource
from models.store import StoreModel
from models.item import ItemModel


class Store(Resource):   # la classe store estende la classe resource (ne puo' utilizzare quindi tutte le funzionalita'
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exist".format(name)}, 400    # .format() riempie le parentesi graffe
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Error'}, 500
        show_store = True
        return store.json(show_store)

    def delete(self, name):
        if StoreModel.find_by_name(name):
            store = StoreModel.find_by_name(name)
            try:
                store.delete_from_db()
            except:
                return {'message': 'Error whit the database'}
            return {'message': 'Store deleted'}
        return {'message': 'Store not find'}


class StoreList(Resource):
    def get(self):
        show_store = False
        return {'stores': [x.json(show_store) for x in StoreModel.query.all()]}


class RemoveItems(Resource):
    def delete(self, id):
        ItemModel.query.filter(ItemModel.store_id == id).delete()
        return {'message': 'All items with store_id = 2 has been removed'}
