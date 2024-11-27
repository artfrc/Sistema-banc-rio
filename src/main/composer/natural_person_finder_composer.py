from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.controllers.natural_person_finder_controller import NaturalPersonFinderController
from src.view.natural_person_finder_controller_view import NaturalPersonFinderControllerView

def natural_person_finder_composer():
    model = NaturalPersonRepository(db_connect_handle)
    controller = NaturalPersonFinderController(model)
    view = NaturalPersonFinderControllerView(controller)

    return view