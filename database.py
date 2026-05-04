import sqlite3

def create_conn():
    return sqlite3.connect('app_data.db')
    
def create_tables():
    conn = create_conn()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
            id INT PRIMARY KEY,
            name TEXT,
            dob DATE,
            level INT,
            xp INT,
            req_xp INT)
    ''')
    
    conn.commit()
    conn.close()
