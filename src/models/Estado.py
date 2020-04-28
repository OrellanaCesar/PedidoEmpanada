


from . import db


class Estado(db.Model):
    __table_name__ = 'estado'
    estado_id = db.Column(db.Integer, primary_key = True)
    estadonombre = db.Column(db.String(80), nullable = False)


    def __init__(self,nombre):
        self.estadonombre = nombre