from src.controllers.interfaces.legal_entity_finder_controller import LegalEntityFinderControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityPersonFinderView(ViewInterface):
    def __init__(self, controller: LegalEntityFinderControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        entity_id = http_request.param["entity_id"]
        body_response = self.__controller.find_entity(entity_id)
        return HttpResponse(status_code=200, body=body_response)