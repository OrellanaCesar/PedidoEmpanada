import sys
sys.append('..')


from run import db


class Estado(db.Model):
    table_name__ = 'estados'
    estado_id = db.Column(db.Integer, primary_key = True)
    estadonombre = db.Column(db.String(80)), nullable = False)


    def __init__(self,nombre):
        self.estadonombre = nombre