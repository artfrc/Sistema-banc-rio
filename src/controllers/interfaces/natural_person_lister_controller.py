from typing import Dict
from abc import ABC, abstractmethod

class NaturalPersonListerControllerInterface(ABC):

   @abstractmethod
   def find_all_entities(self) -> Dict:
      pass