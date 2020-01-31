from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self, show_store):
        if show_store:
            if self.store_id:
                negozio = self.store.name
            else:
                negozio = 'non assegnato'
            return{'name': self.name, 'price': self.price, 'store': negozio}
        else:
            return {'name': self.name, 'price': self.price}



    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # SQLAlchemy fa da solo: connessione al database, e dati estratti sono gia oggetti  -   .first() = solo una riga

    def save_to_db(self):
        db.session.add(self)     # sia update (modificare uno gia' esistente) che insert     #session= insieme di oggetti che vengono aggiunti/aggiornati nel db
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()








