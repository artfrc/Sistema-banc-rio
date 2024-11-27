from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.legal_entity_repository import LegalEntiytRepository
from src.controllers.legal_entity_deleter_controller import LegalEntityDeleterController
from src.view.legal_entity_deleter_controller_view import LegalEntityPersonDeleterView

def legal_entity_person_deleter_composer():
    model = LegalEntiytRepository(db_connect_handle)
    controller = LegalEntityDeleterController(model)
    view = LegalEntityPersonDeleterView(controller)

    return view
