import sys
sys.append('..')


from run import db


class Cliente(db.Model):
    table_name__ = "cliente"
    cliente_id = db.Column(db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(80), nullable=False)
    cliente_direccion = db.Column(db.String(80), nullable=False)
    cliente_telefono = db.Column(db.String(80), nullable=False)

    def __init__(self,nombre,direccion,telefono):
        self.cliente_nombre = nombre
        self.cliente_direccion = direccion
        self.cliente_telefono = telefono

