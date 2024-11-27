from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.natural_person import NaturalPersonTable

class NaturalPersonRepositoryInterface(ABC):
   
   @abstractmethod
   def create_natural_person(self, natural_person: NaturalPersonTable):
      pass
   
   @abstractmethod
   def get_person_by_id(self, entity_id: int):
      pass
   
   @abstractmethod
   def list_all(self) -> List[NaturalPersonTable]:
      pass
   
   @abstractmethod
   def delete_by_id(self, person_id: int):
      pass
   
   @abstractmethod
   def withdraw_money(self, entity_id: int, amount: float):
      pass
   
