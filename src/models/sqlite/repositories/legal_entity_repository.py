from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository_interface import LegalEntityRepositoryInterface

class LegalEntiytRepository(LegalEntityRepositoryInterface):
   def __init__(self, db_connection):
      self.__db_connection = db_connection
      
   def create_entity(self, billing: float, age: int, trade_name: str, phone_number: str, corporate_email: str, category: str, balance: float):
      with self.__db_connection as database:
         try:
            legal_entity = LegalEntityTable(
               billing=billing,
               age=age,
               trade_name=trade_name,
               phone_number=phone_number,
               corporate_email=corporate_email,
               category=category,
               balance=balance
            )
            database.session.add(legal_entity)
            database.session.commit()
         except Exception as exception:
            database.session.rollback()
            raise exception
         
   def get_entity_by_id(self, entity_id: int) -> LegalEntityTable: 
      with self.__db_connection as database:
         try:
            entity = (
               database.session
               .query(LegalEntityTable)
               .filter(LegalEntityTable.id == entity_id)
               .first()
            )
            return entity
            
         except NoResultFound:
            return None
               
      
   def list_all(self) -> List[LegalEntityTable]:
      with self.__db_connection as database:
         try:
            entities = database.session.query(LegalEntityTable).all()
            return entities
         
         except NoResultFound:
            return []
   
   def delete_by_id(self, entity_id: int):
      with self.__db_connection as database:
         try:
            (
               database.session
               .query(LegalEntityTable)
               .filter(LegalEntityTable.id == entity_id)
               .delete()
            )
            database.session.commit()
         except Exception as exception:
            database.session.rollback()
            raise exception
         
   def withdraw_money(self, entity_id: int, new_balance: float) -> LegalEntityTable:
      with self.__db_connection as database:
         try:
            entity = (
               database.session
               .query(LegalEntityTable)
               .filter(LegalEntityTable.id == entity_id)
               .first()
            )
            
            if not entity:
               raise NoResultFound("Entity not found")
            
            entity.balance = new_balance
            database.session.commit()
            
            return entity
         
         except Exception as exception:
            database.session.rollback()
            raise exception