import sqlite3

async def is_admin(tg_id):
    conn = sqlite3.connect('database1.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT user_status FROM users WHERE tg_id = {tg_id}")
    r = cursor.fetchone()
    conn.close()
    return r[0]
