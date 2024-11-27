from .natural_person_lister_controller import NaturalPersonListerController

class MockNaturalPerson:
   def __init__(self, age, name, phone_number, email):
      self.age = age
      self.name = name
      self.phone_number = phone_number
      self.email = email

class MockNaturalPersonRepository:
   def list_all(self):
      return [
         MockNaturalPerson(
            age = 25,
            name = 'John Doe',
            phone_number = '1234567890',
            email = 'john@example.com'
         ),
         MockNaturalPerson(
            age = 30,
            name = 'Jane Doe',
            phone_number = '0987654321',
            email = 'jane@example.com'
         )
      ]

def test_find_all_entities():
   controller = NaturalPersonListerController(MockNaturalPersonRepository())
   response = controller.find_all_entities()
   
   expected_response = {
      'data': {
         'type': 'Natural Person', 
         'count': 2, 
         'attributes': [
            {
               'age': 25, 
               'name': 'John Doe', 
               'phone number': '1234567890', 
               'email': 'john@example.com'}, 
            {
               'age': 30, 
               'name': 'Jane Doe', 
               'phone number': '0987654321', 
               'email': 'jane@example.com'}
            ]
         }
      }
   
   assert response == expected_response