from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .Cliente import Cliente, ClienteSchema
from .Estado import Estado, EstadoSchema
from .Empanadas import Empanadas, EmpanadasSchema
from .Pedidos import Pedidos, PedidosSchema