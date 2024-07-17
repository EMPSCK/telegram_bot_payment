import sqlite3


async def create_user(tg_id, user_name):
    conn = sqlite3.connect('database1.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT id FROM users WHERE tg_id = {tg_id}")
    r = cursor.fetchone()
    if r is not None:
        return

    cursor.execute('INSERT INTO users (tg_id, user_name, user_status, active) VALUES (?, ?, ?, ?)', (tg_id, user_name, '0', '1'))
    conn.commit()
    conn.close()
