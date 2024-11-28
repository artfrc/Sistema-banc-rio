from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.controllers.natural_person_lister_controller import NaturalPersonListerController
from src.view.natural_person_lister_controller_view import NaturalPersonListerControllerView


def natural_person_lister_composer():
    model = NaturalPersonRepository(db_connect_handle)
    controller = NaturalPersonListerController(model)
    view = NaturalPersonListerControllerView(controller)

    return view