#from run import db


class Pedidos(db.Model):


    def __init__(self):
        self.table_name__ = "pedido"
        self.clienteid = db.Column(db.Integer,db.ForeignKey('clienteid', ondelete='CASCADE'), nullable=False))
        self.pedidoid = db.Column(db.Integer, primary_key = True)
        self.pedido_fecha = db.Column(db.DataTime, nullable = False)
        self.pedido_fecha_entrega = db.Column(db.DataTime, nullable = False)
        self.pedido_hora_entrega = horaentrega
        self.pedido_monto = monto
        self.estadoid = db.Column(db.Integer,db.ForeignKey('estadoid', ondelete='CASCADE'), nullable=False))
