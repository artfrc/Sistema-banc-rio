from typing import Dict
from abc import ABC, abstractmethod

class NaturalPersonCreatorControllerInterface(ABC):
   @abstractmethod      
   def create_entity(self, entity_data: Dict) -> Dict:
      pass