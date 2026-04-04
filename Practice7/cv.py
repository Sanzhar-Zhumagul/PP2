from connect import connect
conn = connect()
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")
conn.commit()
cur.close()
conn.close()
print("Table created")