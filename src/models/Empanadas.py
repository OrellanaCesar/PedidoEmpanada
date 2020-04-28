
from . import db
from marshmallow import fields, Schema

class Empanadas(db.Model):


    __table_name__ = 'empanadas'
    empanadas_id = db.Column(db.Integer, primary_key=True)
    empanadas_nombre = db.Column(db.String(80), nullable=False)
    empanadas_cantidad = db.Column(db.Integer, nullable=False)
    empanadas_precio = db.Column(db.Float, nullable=False)


    def __init__(self, nombre, cantidad, precio):
        self.empanadas_nombre = nombre
        self.empanadas_cantidad = cantidad
        self.empanadas_precio = precio


    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    @staticmethod
    def get_all():
        return Empanadas.query.all()


    @staticmethod
    def get_one_cliente(id):
        return Empanadas.query.get(id)


class EmpanadasSchema(Schema):
    empanadas_id = fields.Int(dumo_only=True)
    empanadas_nombre = fields.Str(required=True)
    empanadas_cantidad = fields.Int(required=True)
    empanadas_precio = fields.Float(required=True)