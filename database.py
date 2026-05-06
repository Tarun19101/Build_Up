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
            doj DATE DEFUALT CURRENT_DATE)
    ''')
    
    conn.commit()
    conn.close()
    
def register_user():
    conn = create_conn()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO user (name, dob) VALUES (?, ?)", (name, dob))
    
    conn.commit()
    conn.close()
    
def get_user():
    conn = create_conn()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()
    return user
