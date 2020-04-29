from flask import request, g, Blueprint, json, Response

from ..models.Empanadas import Empanadas, EmpanadasSchema
from marshmallow import ValidationError
empanadas_api = Blueprint('empanadas_api', __name__)
empanadas_schema = EmpanadasSchema()


@empanadas_api.route('/', methods=['POST'])
def create():
    """
    Esta funcion crea una Nueva Empanada. Recibe como parametro 
    por peticcion hhtp el json con los datos
    """

    req_data = request.get_json()
    try:
        data = empanadas_schema.load(req_data)
    except ValidationError as err:
        return custom_response({"messages":"Los Datos de Empanadas son incorrectos"}, 400)
        
    empanada = Empanadas(data)
    empanada.save()
    return custom_response({'message':'Empanada Creada'},201)


@empanadas_api.route('/', methods=['GET'])
def get_all():
    """
    Esta funcion devuelve todos los datos de Empanadas en formato json
    """

    empanada = Empanadas.get_all()
    ser_empanada = empanadas_schema.dump(empanada, many=True)
    return custom_response(ser_empanada,200)


@empanadas_api.route('/<int:empanadas_id>', methods=['GET'])
def get_a_empanada(empanadas_id):
    """
    """
    empanada = Empanadas.get_one_empanada(empanadas_id)
    if not empanada:
        return custom_response({'mesagge':'No existe empanada con ese id'},400)

    ser_emp = empanadas_schema.dump(empanada)
    return custom_response(ser_emp,200)


def custom_response(res, status_code):
  """
  Custom Response Function es el formato de resfuesta http
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
