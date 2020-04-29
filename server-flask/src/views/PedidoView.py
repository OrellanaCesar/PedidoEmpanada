from flask import request, g, Blueprint, json, Response


from ..models.Pedidos import Pedidos,PedidosSchema

from marshmallow import ValidationError

pedido_api = Blueprint('pedido_api', __name__)

pedido_schema = PedidosSchema()


@pedido_api.route('/', methods=['POST'])
def create():
    """
    Esta funcion crea un nuevo pedido. Recibe como parametro
    por peticcion hhtp el json con los datos
    """

    reg_data = request.get_json()
    try:
        data = pedido_schema.load(reg_data)
    except ValidationError :
        return custom_response({'message':'Los datos del Pedido son incorrecto'}, 400)
    pedido = Pedidos(data)
    pedido.save()
    return custom_response({'message':'Pedido Creado'},201)

@pedido_api.route('/', methods=['GET'])
def get_all():
    """
    Esta funcion devuelve todos los pedidos en formato json
    """
    pedido = Pedidos.get_all()
    ser_client = PedidosSchema.dump(pedido, many=True)
    return custom_response(ser_client,200)

def custom_response(res, status_code):
  """
  Custom Response Function es el formato de resfuesta http
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )