from flask import Blueprint, jsonify, request
from src.main.composer.legal_entity_creator_composer import legal_entity_person_creator_composer
from src.main.composer.legal_entity_lister_composer import legal_entity_person_lister_composer
from src.main.composer.legal_entity_deleter_composer import legal_entity_person_deleter_composer

from src.view.http_types.http_request import HttpRequest

legal_entity_bp = Blueprint('legal_entity', __name__)

@legal_entity_bp.route('/legal_entity', methods=['POST'])
def create_person():
    http_request = HttpRequest(body=request.json)
    view = legal_entity_person_creator_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@legal_entity_bp.route('/legal_entity', methods=['GET'])
def list_entities():
    http_request = HttpRequest()
    view = legal_entity_person_lister_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@legal_entity_bp.route('/legal_entity/<id>', methods=['DELETE'])
def delete_entity(entity_id):
    http_request = HttpRequest(param={'entity_id': entity_id})
    view = legal_entity_person_deleter_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code