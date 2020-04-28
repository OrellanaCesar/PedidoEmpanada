from .Pedidos import PedidosSchema
from . import db

from marshmallow import fields, Schema


class Estado(db.Model):
    __table_name__ = 'estado'
    estado_id = db.Column(db.Integer, primary_key = True)
    estado_nombre = db.Column(db.String(80), nullable = False)
    cliente = db.relationship('Pedidos', backref='estado', lazy=True)

    def __init__(self,data):
        self.estadonombre = data.get('estadonombre')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Estado.query.all()

    @staticmethod
    def get_one_estado(id):
        return Estado.query.get(id)


class EstadoSchema(Schema):
    estado_id = fields.Int(dump_only=True)
    estadonombre = fields.Str(required=True)
    cliente = fields.Nested(PedidosSchema, many=True)