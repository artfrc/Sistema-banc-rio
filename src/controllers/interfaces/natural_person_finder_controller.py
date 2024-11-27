from typing import Dict
from abc import ABC, abstractmethod

class NaturalPersonFinderControllerInterface(ABC):
   @abstractmethod
   def find_entity(self, entity_id: int) -> Dict:
        pass
