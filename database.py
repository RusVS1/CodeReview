import sqlite3

def update_database(frame_name, prices):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS frames (
    frame TEXT PRIMARY KEY,
    sets INTEGER,
    blueprint INTEGER,
    neuroptics INTEGER,
    systems INTEGER,
    chassis INTEGER
    )
    """)
    connection.commit()
    frame = (frame_name, prices[0], prices[1], prices[2], prices[3], prices[4])
    connection.commit()
    cursor.execute("""INSERT or REPLACE INTO frames VALUES(?, ?, ?, ?, ?, ?);""", frame)
    connection.commit()
    connection.close()

def get_prices(frame_name):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM frames WHERE frame = ?', (frame_name,))
    prices = cursor.fetchone()
    connection.close()
    return prices

