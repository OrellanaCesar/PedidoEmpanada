from flask import Flask, render_template, request, redirect, url_for, abort
from .models import db

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:orellana@localhost:5432/PedidosEmpanadasFlask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    @app.route("/",methods=['GET'])
    def index():
        return 'Felicidades sos el primer emdpoit trabajando'

    return app