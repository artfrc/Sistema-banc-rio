from .legal_entity_withdraw_money_controller import LegalEntityWithdrawMoneyController

class MockEntity:
   def __init__(self, entity_id, trade_name, balance):
      self.entity_id = entity_id
      self.trade_name = trade_name
      self.balance = balance

class MockLegalEntityRepository():
   
   def withdraw_money(self, entity_id: int, amount: float): #pylint: disable= W0613, unused-argument
      return MockEntity(
         entity_id = 1, 
         trade_name = "Enterprise ABC", 
         balance = 1000 - amount)
   
   def get_entity_by_id(self, entity_id: int): #pylint: disable= W0613, unused-argument
      return MockEntity(
         entity_id = 1, 
         trade_name = "Enterprise ABC", 
         balance = 1000.0)

def test_withdraw_money():
   controller = LegalEntityWithdrawMoneyController(MockLegalEntityRepository())
   response = controller.withdraw_money(1, 500.0)
   
   expected_response = {
      'data': {
         'type': 'Legal Entity', 
         'count': 1, 
         'attributes': {
            'trade_name': 'Enterprise ABC', 
            'balance': 500.0
            }
         }
      }
   
   assert response == expected_response