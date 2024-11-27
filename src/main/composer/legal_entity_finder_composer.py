from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.legal_entity_repository import LegalEntiytRepository
from src.controllers.legal_entity_finder_controller import LegalEntityFinderController
from src.view.legal_entity_finder_controller_view import LegalEntityPersonFinderView

def legal_entity_finder_composer():
    model = LegalEntiytRepository(db_connect_handle)
    controller = LegalEntityFinderController(model)
    view = LegalEntityPersonFinderView(controller)

    return view