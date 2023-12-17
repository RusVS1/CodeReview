import psycopg2

def update_database(frame_name, prices):
    connection = psycopg2.connect(
        host="db",
        user="root",
        password="root",
        port="5432",
        dbname="frames"
    )
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
    cursor.execute("""
        INSERT INTO frames (frame, sets, blueprint, neuroptics, systems, chassis)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (frame) DO UPDATE
        SET sets = EXCLUDED.sets,
            blueprint = EXCLUDED.blueprint,
            neuroptics = EXCLUDED.neuroptics,
            systems = EXCLUDED.systems,
            chassis = EXCLUDED.chassis;
    """, frame)
    connection.commit()
    connection.close()

def get_prices(frame_name):
    connection = psycopg2.connect(
        host="db",
        user="root",
        password="root",
        port="5432",
        dbname="frames"
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM frames WHERE frame = %s', (frame_name,))
    prices = cursor.fetchone()
    connection.close()
    return prices

