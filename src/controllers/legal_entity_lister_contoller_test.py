from .legal_entity_lister_controller import LegalEntityListerController

class MockEntity:
   def __init__(self, age, trade_name, phone_number, corporate_email, category):
      self.age = age
      self.trade_name = trade_name
      self.phone_number = phone_number
      self.corporate_email = corporate_email
      self.category = category

class MockEntityRepository:
   def list_all(self):
      return [
         MockEntity(
            age = 25,
            trade_name = 'John Doe',
            phone_number = '1234567890',
            corporate_email = 'john@example.com',
            category = 'Legal Entity'
         ),
         MockEntity(
            age = 30,
            trade_name = 'Jane Doe',
            phone_number = '0987654321',
            corporate_email = 'jane@example.com',
            category = 'Legal Entity'
         )
      ]

def test_find_all_entities():
   controller = LegalEntityListerController(MockEntityRepository())
   response = controller.find_all_entities()
   
   expected_response = {
      'data': {
         'type': 'Legal Entity', 
         'count': 2, 
         'attributes': [
            {
               'age': 25, 
               'trade name': 'John Doe', 
               'phone number': '1234567890', 
               'corporate email': ('john@example.com')}, 
            {
               'age': 30, 
               'trade name': 'Jane Doe', 
               'phone number': '0987654321', 
               'corporate email': ('jane@example.com')
               }
            ]
         }
      }
   
   assert response == expected_response