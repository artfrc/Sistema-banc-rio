from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityFinderControllerInterface(ABC):
   @abstractmethod
   def find_entity(self, entity_id: int) -> Dict:
      pass