from src.models.sqlite.settings.connection import db_connect_handle
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.controllers.natural_person_deleter_controller import NaturalPersonDeleterController
from src.view.natural_person_deleter_controller_view import NaturalPersonDeleterControllerView

def natural_person_deleter_composer():
    model = NaturalPersonRepository(db_connect_handle)
    controller = NaturalPersonDeleterController(model)
    view = NaturalPersonDeleterControllerView(controller)

    return view