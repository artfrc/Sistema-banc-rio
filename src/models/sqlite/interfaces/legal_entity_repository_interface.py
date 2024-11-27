from abc import ABC, abstractmethod
from typing import List

from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityRepositoryInterface(ABC):
   
   @abstractmethod
   def create_entity(self, billing: float, age: int, trade_name: str, phone_number: str, corporate_email: str, category: str, balance: float):
      pass
   
   @abstractmethod
   def get_entity_by_id(self, entity_id: int):
      pass
   
   @abstractmethod
   def list_all(self) -> List[LegalEntityTable]:
      pass
   
   @abstractmethod
   def delete_by_id(self, entity_id: int):
      pass
   
   @abstractmethod
   def withdraw_money(self, entity_id: int, amount: float):
      pass