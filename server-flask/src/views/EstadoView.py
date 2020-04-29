from flask import request, g, Blueprint, json, Response


from ..models.Estado import Estado, EstadoSchema

from marshmallow import ValidationError

estado_api = Blueprint('estado_api', __name__)

estado_schema = EstadoSchema()

@estado_api.route('/', methods=['POST'])
def create():
    """
    Esta funcion crea un nuevo estado. Recibe como parametro
    por peticcion hhtp el json con los datos
    """

    reg_data = request.get_json()
    try:
        data = estado_schema.load(reg_data)
    except ValidationError :
        return custom_response({'message':'Los datos del Estado son incorrecto'}, 400)
    estado = Estado(data)
    estado.save()
    return custom_response({'message':'Estado Creado'},201)


@estado_api.route('/', methods=['GET'])
def get_all():
    """
    Esta funcion devuelve todos los estados en formato json
    """
    estado = Estado.get_all()
    ser_client = EstadoSchema.dump(estado, many=True)
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
