from typing import Dict
import re
from src.models.sqlite.interfaces.legal_entity_repository_interface import LegalEntityRepositoryInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityWithdrawMoneyController:
    def __init__(self, entity_repository: LegalEntityRepositoryInterface):
        self.__entity_repository = entity_repository
        self.__max_amount = 1000000

    def withdraw_money(self, entity_id: int, amount: float) -> Dict:
        self.__validate_entity_id(entity_id)
        entity = self.__validate_get_entity(entity_id)
        self.__validate_amount(amount)
        self.__validate_amount_entity(entity, amount)
        new_balance = self.__calculate_new_balance_entity(entity, amount)
        entity = self.__entity_repository.withdraw_money(entity_id, new_balance)

        return self.__format_response(entity)

    def __validate_entity_id(self, entity_id: int):
        if entity_id < 0:
            raise Exception('Entity ID must be greater than 0')

        no_valid_characters = re.compile(r'[^0-9]')
        if no_valid_characters.search(str(entity_id)):
            raise Exception('Entity ID must be a number')

    def __validate_amount(self, amount: float):
        if amount < 0:
            raise Exception('Amount must be greater than 0')
        
        if amount > self.__max_amount:
            raise Exception(f'Amount must be less than {self.__max_amount}')

        no_valid_characters = re.compile(r'[^0-9.]')
        if no_valid_characters.search(str(amount)):
            raise Exception('Amount must be a number and a dot. Ex: 100.00')

    def __validate_get_entity(self, entity_id: int):
        entity = self.__entity_repository.get_entity_by_id(entity_id)
        if not entity:
            raise Exception('Entity not found')
        return entity

    def __validate_amount_entity(self, entity: LegalEntityTable, amount: float):
        if entity.balance < amount:
            raise Exception('Insufficient funds')
            
    def __calculate_new_balance_entity(self, entity: LegalEntityTable, amount: float) -> float:
        new_balance = entity.balance - amount
        
        return new_balance

    def __format_response(self, entity_data: LegalEntityTable) -> Dict:
        return {
            "data": {
                "type": "Legal Entity",
                "count": 1,
                "attributes": {
                    "trade_name": entity_data.trade_name,
                    "balance": entity_data.balance
                }
            }
        }