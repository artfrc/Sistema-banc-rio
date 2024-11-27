from abc import ABC, abstractmethod

class NaturalPersonDeleterControllerInterface(ABC):
   @abstractmethod
   def delete(self, entity_id: int):
      pass