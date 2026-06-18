from connection import cursor,connect
from table_creation import table_creation
import time

class Transactions:

    def __init__(self,value,type,category,description):
        self.value = value
        self.type = type
        self.category = category
        self.description = description

    def create (self):
        cursor.execute("""
        INSERT INTO transactions (description,category,value,type)
        values (%s,%s,%s,%s)
        """,(self.description,self.category,self.value,self.type))

        connect.commit()
        time.sleep(3)
        print('Dados inseridos com sucesso')


new_transaction = Transactions('600.50', 'RECEITA','VENDA','VENDA REALIZADA DE FORMA ONLINE')
new_transaction.create()
    
        






