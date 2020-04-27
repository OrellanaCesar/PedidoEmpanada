


from run import db


class DetallePedido(db.Model):
    table_name__ = "detallepedido"
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