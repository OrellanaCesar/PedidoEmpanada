from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from Estado import Estado

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:orellana@localhost:5432/PedidosEmpanadasFlask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
session_options = {'autocommit': False, 'autoflush': False}

#login_manager = LoginManager(app)
#login_manager.login_view = "login"

db = SQLAlchemy(app,session_options = session_options)

db.create_all()

