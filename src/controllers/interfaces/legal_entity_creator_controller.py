from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityCreatorControllerInterface(ABC):
   @abstractmethod
   def create_entity(self, entity_data: Dict) -> Dict:
      pass