import sqlite3

def get_user_list():
    conn = sqlite3.connect('database1.db')
    cursor = conn.cursor()
    cursor.execute(f'select * from users')
    r = cursor.fetchall()
    conn.commit()
    conn.close()
    return r
