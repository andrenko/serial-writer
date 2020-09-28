from app.api import bp
from app.api.errors import bad_request
from app.models import Data
from port_controller import Serial
from flask import jsonify, request


@bp.route('/data/', methods=['GET'])
def get_data():
    data = Data(Serial().in_waiting(), Serial().read(10))
    return jsonify(data.to_dict())


@bp.route('/data/', methods=['POST'])
def post_data():
    data = request.get_json() or {}
    if 'string' not in data:
        return bad_request("request must include 'string' field")
    Serial().write(data['string'])
    response = jsonify(Data(Serial().in_waiting(), data['string']).to_dict())
    response.status_code = 201
    return response
