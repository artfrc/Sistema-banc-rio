from abc import ABC, abstractmethod

class LegalEntityDeleterControllerInterface(ABC):
   @abstractmethod   
   def delete(self, entity_id: int):
      pass