from src.controllers.interfaces.natural_person_lister_controller import NaturalPersonListerControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class NaturalPersonListerControllerView(ViewInterface):
    def __init__(self, controller: NaturalPersonListerControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.find_all_entities()
        return HttpResponse(200, body_response)