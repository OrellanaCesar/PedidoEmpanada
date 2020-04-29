from flask import Flask, render_template, request, redirect, url_for, abort
from .models import db
from .views.EmpanadasView import empanadas_api as empanadas_blueprint
from .views.ClienteView import cliente_api as cliente_blueprint
from .views.EstadoView import estado_api as estado_blueprint
from .views.PedidoView import pedido_api as pedido_blueprint
from .views.DetallePedidoView import detalle_api as detalle_blueprint

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:orellana@localhost:5432/PedidosEmpanadasFlask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(empanadas_blueprint, url_prefix='/api/v1/empanadas')
    app.register_blueprint(cliente_blueprint, url_prefix='/api/v1/clientes')
    app.register_blueprint(estado_blueprint,url_prefix='/api/v1/estados')
    app.register_blueprint(pedido_blueprint,url_prefix='/api/v1/pedidos')
    app.register_blueprint(detalle_blueprint,url_prefix='/api/v1/detallepedido')
    @app.route("/",methods=['GET'])
    def index():
        return 'Felicidades sos el primer emdpoit trabajando'

    return app

