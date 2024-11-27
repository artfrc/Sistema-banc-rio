from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityListerControllerInterface(ABC):
   @abstractmethod
   def find_all_entities(self) -> Dict:
      pass