from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self, show_store):
        return{'name': self.name, 'items': [item.json(show_store) for item in self.items.all()]}

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