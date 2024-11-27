from typing import Dict, List
from src.models.sqlite.interfaces.natural_person_repository_interface import NaturalPersonRepositoryInterface
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from .interfaces.natural_person_lister_controller import NaturalPersonListerControllerInterface

class NaturalPersonListerController(NaturalPersonListerControllerInterface):
   def __init__(self, entity_repository: NaturalPersonRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def find_all_entities(self) -> Dict:
      entities = self.__find_all_entities_in_db()
      return self.__format_response_for_all_entities(entities)
   
   def __find_all_entities_in_db(self) -> List[NaturalPersonTable]:
      entities = self.__entity_repository.list_all()
      
      if not entities:
         raise Exception('No entities found')
      
      return entities
   
   def __format_response_for_all_entities(self, entities: List[NaturalPersonTable]) -> Dict:
      return {
         "data": {
            "type": "Natural Person",
            "count": len(entities),
            "attributes": [
               {
                  "age": entity.age,
                  "name": entity.name,
                  "phone number": entity.phone_number,
                  "email": entity.email,
               }
               for entity in entities
            ]
         }
      }