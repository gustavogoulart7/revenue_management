from connection import cursor

def table_creation ():
    cursor.execute("""
        CREATE TABLE transactions (
            id SERIAL PRIMARY KEY,
            transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description VARCHAR (255),
            category VARCHAR (100),
            value NUMERIC (10,2),
            type VARCHAR (10));
        """)

print("Table Created")