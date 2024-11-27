from src.controllers.interfaces.legal_entity_deleter_controller import LegalEntityDeleterControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityPersonDeleterView(ViewInterface):
    def __init__(self, controller: LegalEntityDeleterControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        entity_id = http_request.param["entity_id"]
        self.__controller.delete(entity_id)
        return HttpResponse(status_code=204, body=None)