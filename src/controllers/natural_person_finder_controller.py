from typing import Dict
from src.models.sqlite.interfaces.natural_person_repository_interface import NaturalPersonRepositoryInterface
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from .interfaces.natural_person_finder_controller import NaturalPersonFinderControllerInterface

class NaturalPersonFinderController(NaturalPersonFinderControllerInterface):
   def __init__(self, entity_repository: NaturalPersonRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def find_entity(self, entity_id: int) -> Dict:
      entity = self.__find_entity_in_db(entity_id)
      return self.__format_response_for_entity(entity)
   
   def __find_entity_in_db(self, entity_id: int) -> NaturalPersonTable:
      entity = self.__entity_repository.get_person_by_id(entity_id)
      if not entity:
         raise Exception('Entity not found')
      
      return entity
   
   def __format_response_for_entity(self, entity: NaturalPersonTable) -> Dict:
      return {
         "data": {
            "type": "Natural Person",
            "count": 1,
            "attributes": {
               "age": entity.age,
               "name": entity.name,
               "phone number": entity.phone_number},
               "email": entity.email,
         }
      }