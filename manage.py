import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import db, crear_app

app = crear_app()
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from src.models import Cliente, Empanadas, Pedidos, Estado, DetallePedido

if __name__ == '__main__':
    manager.run()
