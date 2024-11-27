from src.controllers.interfaces.natural_person_creator_controller import NaturalPersonCreatorControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class NaturalPersonListerControllerView(ViewInterface):
    def __init__(self, controller: NaturalPersonCreatorControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person_info = http_request.body
        body_response = self.__controller.create_entity(natural_person_info)
        return HttpResponse(status_code=201, body=body_response)