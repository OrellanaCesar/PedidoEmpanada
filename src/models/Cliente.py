from .Pedidos import PedidosSchema
from . import db
from marshmallow import fields, Schema

class Cliente(db.Model):
    __table_name__ = "cliente"
    cliente_id = db.Column(db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(80), nullable=False)
    cliente_direccion = db.Column(db.String(80), nullable=False)
    cliente_telefono = db.Column(db.String(80), nullable=False)
    pedido = db.relationship('Pedido', backref='cliente', lazy=True)

    def __init__(self,data):
        self.cliente_nombre = data.get('cliente_nombre')
        self.cliente_direccion = data.get('cliente_direccion')
        self.cliente_telefono = data.get('cliente_telefono')

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    @staticmethod
    def get_all():
        return Cliente.query.all()

    
    @staticmethod
    def get_one_cliente(id):
        return Cliente.query.get(id)

class ClienteSchema(Schema):
    cliente_id = fields.Int(dumo_only=True)
    cliente_nombre = fields.Str(required=True)
    cliente_direccion = fields.Str(required=True)
    cliente_telefono = fields.Str(required=True)
    pedido = fields.Nested(PedidosSchema, many=True)