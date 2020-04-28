
from . import db
from marshmallow import fields, Schema

class DetallePedido(db.Model):
    __table_name__ = "detallepedido"
    detallepedido_id = db.Column(db.Integer, primary_key = True)
    empanadas_id = db.Column(db.Integer, db.ForeignKey('empanadas.empanadas_id', ondelete ='CASCADE'), nullable = False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id', ondelete ='CASCADE'), nullable = False)
    detalle_cantidad = db.Column(db.Integer, nullable = False)
    detalle_descripcion = db.Column(db.Text, nullable = False)
    detalle_total = db.Column(db.Float, nullable = False)


    def __init__(self,cantidad,descripcion,total):
        self.detalle_cantidad = cantidad
        self.detalle_descripcion = descripcion
        self.detalle_total = total


    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    @staticmethod
    def get_all():
        return DetallePedido.query.all()


    @staticmethod
    def get_one_cliente(id):
        return DetallePedido.query.get(id)


class DetallePedidoSchema(Schema):
    detallepedido_id = fields.Int(dumo_only=True)
    empanadas_id = fields.Int(dumo_only=True)
    pedido_id = fields.Int(dumo_only=True)
    detalle_cantidad = fields.Int(required=True)
    detalle_descripcion = fields.String(required=True)
    detalle_total = fields.Float(required=True)
   