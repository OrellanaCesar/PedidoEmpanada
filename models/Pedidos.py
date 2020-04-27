import sys
sys.append('..')


from run import db


class Pedidos(db.Model):
    table_name__ = "pedido"
    clienteid = db.Column(db.Integer, db.ForeignKey('cliente_id', ondelete = 'CASCADE'), nullable = False))
    pedido_id = db.Column(db.Integer, primary_key = True)
    pedido_fecha = db.Column(db.DataTime, nullable = False)
    pedido_fecha_entrega = db.Column(db.DataTime, nullable = False)
    pedido_hora_entrega = db.Column(db.DataTime, nullable = False)
    pedido_monto = db.Column(db.Float, nullable = False)
    estadoid = db.Column(db.Integer, db.ForeignKey('estado_id', ondelete ='CASCADE'), nullable = False))

    def __init__(self,fecha,fechaentrega,fechahora,monto):
        self.pedido_fecha = fecha
        self.pedido_fecha_entrega = fechaentrega
        self.pedido_hora_entrega = fechahora
        self.pedido_monto = monto

