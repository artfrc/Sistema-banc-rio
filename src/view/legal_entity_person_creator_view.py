from src.controllers.interfaces.legal_entity_creator_controller import LegalEntityCreatorControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityPersonCreatorView(ViewInterface):
    def __init__(self, controller: LegalEntityCreatorControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_info = http_request.body
        body_response = self.__controller.create_entity(legal_entity_info)
        return HttpResponse(status_code=201, body=body_response)
