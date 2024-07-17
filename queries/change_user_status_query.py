import sqlite3


async def change_user_status(tg_id):
    conn = sqlite3.connect('database1.db')
    cursor = conn.cursor()

    cursor.execute(f'Update users set user_status = 1 where tg_id = {tg_id}')
    conn.commit()
    conn.close()