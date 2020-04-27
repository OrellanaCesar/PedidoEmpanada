
from run import db


class Empanadas(db.Model):
    table_name__ = 'empanadas'
    empanadas_id = db.Column(db.Integer, primary_key=True)
    empanadas_nombre = db.Column(db.String(80), nullable=False)
    empanadas_cantidad = db.Column(db.Integer, nullable=False)
    empanadas_precio = db.Column(db.Float, nullable=False)

    def __init__(self, nombre, cantidad, precio):
        self.empanadas_nombre = nombre
        self.empanadas_cantidad = cantidad
        self.empanadas_precio = precio