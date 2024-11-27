from src.controllers.interfaces.natural_person_finder_controller import NaturalPersonFinderControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class NaturalPersonFinderControllerView(ViewInterface):
    def __init__(self, controller: NaturalPersonFinderControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person_id = http_request.param["natural_person_id"]
        body_response = self.__controller.find_natural_person(natural_person_id)
        return HttpResponse(status_code=200, body=body_response)