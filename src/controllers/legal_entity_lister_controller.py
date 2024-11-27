from typing import Dict, List
from src.models.sqlite.interfaces.legal_entity_repository_interface import LegalEntityRepositoryInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .interfaces.legal_entity_lister_controller import LegalEntityListerControllerInterface

class LegalEntityListerController(LegalEntityListerControllerInterface):
   def __init__(self, entity_repository: LegalEntityRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def find_all_entities(self) -> Dict:
      entities = self.__find_all_entities_in_db()
      return self.__format_response_for_all_entities(entities)
   
   def __find_all_entities_in_db(self) -> List[LegalEntityTable]:
      entities = self.__entity_repository.list_all()
      
      if not entities:
         raise Exception('No entities found')
      
      return entities
   
   def __format_response_for_all_entities(self, entities: List[LegalEntityTable]) -> Dict:
      return {
         "data": {
            "type": "Legal Entity",
            "count": len(entities),
            "attributes": [
               {
                  "age": entity.age,
                  "trade name": entity.trade_name,
                  "phone number": entity.phone_number,
                  "corporate email": entity.corporate_email,
               }
               for entity in entities
            ]
         }
      }      