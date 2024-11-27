from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.legal_entity_repository import LegalEntiytRepository
from src.controllers.legal_entity_creator_controller import LegalEntityCreatorController
from src.view.legal_entity_person_creator_view import LegalEntityPersonCreatorView

def legal_entity_person_creator_composer():
    model = LegalEntiytRepository(db_connect_handle)
    controller = LegalEntityCreatorController(model)
    view = LegalEntityPersonCreatorView(controller)

    return view