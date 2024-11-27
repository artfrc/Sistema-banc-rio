from .natural_person_withdraw_money_controller import NaturalPersonWithdrawMoneyController

class MockEntity:
   def __init__(self, entity_id, name, balance):
      self.entity_id = entity_id
      self.name = name
      self.balance = balance

class MockLegalEntityRepository():
   
   def withdraw_money(self, entity_id: int, amount: float): #pylint: disable= W0613, unused-argument
      return MockEntity(
         entity_id = 1, 
         name = "Enterprise ABC", 
         balance = 1000 - amount)
   
   def get_entity_by_id(self, entity_id: int): #pylint: disable= W0613, unused-argument
      return MockEntity(
         entity_id = 1, 
         name = "Enterprise ABC", 
         balance = 1000.0)

def test_withdraw_money():
   controller = NaturalPersonWithdrawMoneyController(MockLegalEntityRepository())
   response = controller.withdraw_money(1, 500.0)
   
   expected_response = {
      'data': {
         'type': 'Natural Person', 
         'count': 1, 
         'attributes': {
            'name': 'Enterprise ABC', 
            'balance': 500.0
            }
         }
      }
   
   assert response == expected_response