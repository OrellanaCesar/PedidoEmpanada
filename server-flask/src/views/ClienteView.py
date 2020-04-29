from flask import request, g, Blueprint, json, Response

from ..models.Cliente import Cliente, ClienteSchema
from marshmallow import ValidationError

cliente_api = Blueprint('cliente_api', __name__)
cliente_schema = ClienteSchema()

@cliente_api.route('/', methods=['POST'])
def create():
    """
    Esta funcion crea un nuevo cliente. Recibe como parametro 
    por peticcion hhtp el json con los datos
    """

    req_data = request.get_json()
    try:
        data = cliente_schema.load(req_data)
    except ValidationError as err:
        return custom_response({"message":"Los Datos de Clientes son incorrectos"}, 400)
    client = Cliente(data)
    client.save()
    return custom_response({'message':'Cliente Creado'},201)


@cliente_api.route('/', methods=['GET'])
def get_all():
    """
    Esta funcion devuelve todos los clientes en formato json
    """

    client = Cliente.get_all()
    ser_client = cliente_schema.dump(client, many=True)
    return custom_response(ser_client,200)


@cliente_api.route('/<int:clientes_id>', methods=['GET'])
def get_a_cliente(clientes_id):
    """
    """
    client = Cliente.get_one_cliente(clientes_id)
    if not client:
        return custom_response({'mesagge':'No existe Cliente con ese id'},400)

    ser_cli = cliente_schema.dump(client)
    return custom_response(ser_cli,200)


def custom_response(res, status_code):
  """
  Custom Response Function es el formato de resfuesta http
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
