from . import db

from marshmallow import fields, Schema

class Pedidos(db.Model):
    __table_name__ = "pedidos"
    pedido_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id', ondelete = 'CASCADE'), nullable = False)
    pedido_fecha = db.Column(db.DateTime, nullable = False)
    pedido_fecha_entrega = db.Column(db.DateTime, nullable = False)
    pedido_hora_entrega = db.Column(db.DateTime, nullable = False)
    pedido_monto = db.Column(db.Float, nullable = False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.estado_id', ondelete ='CASCADE'), nullable = False)

    def __init__(self,fecha,fechaentrega,fechahora,monto):
        self.pedido_fecha = fecha
        self.pedido_fecha_entrega = fechaentrega
        self.pedido_hora_entrega = fechahora
        self.pedido_monto = monto

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Pedidos.query.all()

    @staticmethod
    def get_one_cliente(id):
        return Pedidos.query.get(id)


class PedidosSchema(Schema):
    cliente_id = fields.Int(dumo_only=True)
    cliente_nombre = fields.Str(required=True)
    cliente_direccion = fields.Str(required=True)
    cliente_telefono = fields.Str(required=True)
    pedido_id = fields.Int(dump_only=True)
    cliente_id = fields.Int(dump_only=True)
    pedido_fecha = fields.DateTime(dump_only=True)
    pedido_fecha_entrega = fields.DateTime(dump_only=True)
    pedido_hora_entrega = fields.DateTime(dump_only=True)
    pedido_monto = fields.Float(required=True)
    estado_id = fields.Int(dumo_only=True)