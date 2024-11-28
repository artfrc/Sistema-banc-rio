from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.natural_person_finder_composer import natural_person_finder_composer
from src.main.composer.natural_person_creator_composer import natural_person_creator_composer

natural_person_bp = Blueprint('natural_person', __name__)

@natural_person_bp.route('/natural_person/<natural_person_id>', methods=['GET'])
def get_person(natural_person_id):
    http_request = HttpRequest(param={'natural_person_id': natural_person_id})
    view = natural_person_finder_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@natural_person_bp.route('/natural_person', methods=['POST'])
def create_person():
    http_request = HttpRequest(body=request.json)
    view = natural_person_creator_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
