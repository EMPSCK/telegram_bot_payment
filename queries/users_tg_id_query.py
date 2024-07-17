import sqlite3


async def get_users_tg_id():
    conn = sqlite3.connect('database1.db')
    cursor = conn.cursor()
    cursor.execute(f'select tg_id from users')
    r = cursor.fetchall()
    conn.commit()
    conn.close()
    return r
