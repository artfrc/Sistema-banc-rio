from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityWithdrawMoneyControllerInterface(ABC):
    @abstractmethod
    def withdraw_money(self, entity_id: int, amount: float) -> Dict:
        pass