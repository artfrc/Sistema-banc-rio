from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.legal_entity_repository import LegalEntiytRepository
from src.controllers.legal_entity_withdraw_money_controller import LegalEntityWithdrawMoneyController
from src.view.legal_entity_with_draw_money_view import LegalEntityWithdrawMoneyView

def legal_entity_person_withdaw_money_composer():
    model = LegalEntiytRepository(db_connect_handle)
    controller = LegalEntityWithdrawMoneyController(model)
    view = LegalEntityWithdrawMoneyView(controller)

    return view