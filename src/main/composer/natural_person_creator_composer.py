from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.controllers.natural_person_creator_controller import NaturalPersonCreatorController
from src.view.natural_person_person_creator_view import NaturalPersonListerControllerView


def natural_person_creator_composer():
    model = NaturalPersonRepository(db_connect_handle)
    controller = NaturalPersonCreatorController(model)
    view = NaturalPersonListerControllerView(controller)

    return view