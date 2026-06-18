from connection import cursor, connect

def create(value, type, category, description):
    cursor.execute("""
    INSERT INTO transactions (description, category, value, type)
    VALUES (%s, %s, %s, %s)
    """, (description, category, value, type))
    connect.commit()
    print('Dados inseridos com sucesso!')

def read():
    cursor.execute("SELECT id, transaction_date, value, description FROM transactions")
    return cursor.fetchall()  # Retorna a lista para o arquivo da tela decidir como mostrar

def update(transaction_id, new_value):
    cursor.execute("""
    UPDATE transactions SET value = %s WHERE id = %s
    """, (new_value, transaction_id))
    connect.commit()
    print('Dados atualizados com sucesso!')

def delete(transaction_id):
    cursor.execute("DELETE FROM transactions WHERE id = %s", (transaction_id,))
    connect.commit()
    print("Transação deletada com sucesso!")