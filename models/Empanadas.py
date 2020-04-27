import sys
sys.append('..')
from run import db


class Emapanadas(db.Model):
    table_name__ = "emapanadas"
    empanadas_id = db.Column(db.Integer, primary_key=True)
    empanadas_nombre = db.Column(db.String(80), nullable=False)
    empanadas_cantidad = db.Column(db.String(80), nullable=False)
    empanadas_precio = db.Column(db.String(80), nullable=False)

    def __init__(self):
        self.table_name__ = "cliente"
        self.cliente_id = db.Column(db.Integer, primary_key = True)
        self.cliente_nombre = db.Column(db.String(80),nullable = False)
        self.cliente_direccion = db.Column(db.String(80),nullable = False)
        self.cliente_telefono = db.Column(db.String(80),nullable = False)
#        self.__tipo_datos = ['int', 'string', 'string', 'string']