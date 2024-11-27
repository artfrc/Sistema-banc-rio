from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.legal_entity_repository import LegalEntiytRepository
from src.controllers.legal_entity_lister_controller import LegalEntityListerController
from src.view.legal_entity_lister_controller_view import LegalEntityPersonListerView

def legal_entity_person_lister_composer():
    model = LegalEntiytRepository(db_connect_handle)
    controller = LegalEntityListerController(model)
    view = LegalEntityPersonListerView(controller)

    return view
