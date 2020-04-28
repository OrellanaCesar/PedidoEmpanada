from run import db

from Estado import Estado
from Empanadas import Empanadas

pendiente = Estado('PENDIENTE')
entregado = Estado('ENTREGADO')
cancelado = Estado('CANCELADO')
carne = Empanadas('CARNE',0,250.0)
pollo = Empanadas('POLLO',0,250.0)


db.session.add(pendiente)
db.session.add(entregado)
db.session.add(cancelado)
db.session.add(carne)
db.session.add(pollo)
db.session.commit()

