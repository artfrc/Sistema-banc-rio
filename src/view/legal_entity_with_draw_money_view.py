from src.controllers.interfaces.legal_entity_withdraw_money_controller import LegalEntityWithdrawMoneyControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityWithdrawMoneyView(ViewInterface):
    def __init__(self, controller:  LegalEntityWithdrawMoneyControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_id = http_request.body['entity_id']
        legal_entity_amount = http_request.body['amount']
        body_response = self.__controller.withdraw_money(legal_entity_id, legal_entity_amount)
        return HttpResponse(status_code=200, body=body_response)
        