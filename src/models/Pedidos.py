

from . import db


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

