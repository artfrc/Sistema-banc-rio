from src.controllers.interfaces.legal_entity_lister_controller import LegalEntityListerControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityPersonListerView(ViewInterface):
    def __init__(self, controller: LegalEntityListerControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.find_all_entities()
        return HttpResponse(status_code=200, body=body_response)