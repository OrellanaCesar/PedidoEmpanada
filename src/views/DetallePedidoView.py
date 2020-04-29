from flask import request, g, Blueprint, json, Response


from ..models.DetallePedido import DetallePedido,DetallePedidoSchema

from marshmallow import ValidationError

detalle_api = Blueprint('detalle_api', __name__)

detalle_schema = DetallePedidoSchema()

@detalle_api.route('/', methods=['POST'])
def create():
    """
    Esta funcion crea un nuevo detalle del pedido. Recibe como parametro
    por peticcion hhtp el json con los datos
    """

    reg_data = request.get_json()
    try:
        data = detalle_schema.load(reg_data)
    except ValidationError :
        return custom_response({'message':'Los datos del Detalle del Pedido son incorrecto'}, 400)
    detalle = DetallePedido(data)
    detalle.save()
    return custom_response({'message':'Pedido Creado'},201)


@detalle_api.route('/', methods=['GET'])
def get_all():
    """
    Esta funcion devuelve todos los detalles de un pedido en formato json
    """
    detalle = DetallePedido.get_all()
    ser_client = DetallePedidoSchema.dump(detalle, many=True)
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
