from run import db
class Cliente(db.Model):
    table_name__ = "cliente"
    cliente_id = db.Column(db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(80), nullable=False)
    cliente_direccion = db.Column(db.String(80), nullable=False)
    cliente_telefono = db.Column(db.String(80), nullable=False)

    def __init__(self):
        self.table_name__ = "cliente"
        self.cliente_id = db.Column(db.Integer, primary_key = True)
        self.cliente_nombre = db.Column(db.String(80),nullable = False)
        self.cliente_direccion = db.Column(db.String(80),nullable = False)
        self.cliente_telefono = db.Column(db.String(80),nullable = False)
#        self.__tipo_datos = ['int', 'string', 'string', 'string']
