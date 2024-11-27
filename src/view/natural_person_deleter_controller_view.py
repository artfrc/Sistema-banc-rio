from src.controllers.interfaces.natural_person_deleter_controller import NaturalPersonDeleterControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class NaturalPersonDeleterControllerView(ViewInterface):
    def __init__(self, controller: NaturalPersonDeleterControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["person_id"]
        self.__controller.delete(person_id)
        return HttpResponse(status_code=204, body=None)
        