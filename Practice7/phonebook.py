import csv
from connect import connect
# ---------- CREATE TABLE ----------
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20) UNIQUE
    );
    """)
    conn.commit()
    cur.close()
    conn.close()

# ---------- INSERT FROM CSV ----------
def insert_csv():
    conn = connect()
    cur = conn.cursor()
    with open("contacts.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (row['name'], row['phone'])
                )
            except:
                print("Duplicate skipped:", row)
    conn.commit()
    cur.close()
    conn.close()

# ---------- INSERT FROM INPUT ----------
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO contacts VALUES (DEFAULT, %s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Added")
    except:
        print("Error (maybe duplicate phone)")
    cur.close()
    conn.close()

# ---------- UPDATE ----------
def update():
    name = input("Find by name: ")
    new_name = input("New name (or enter to skip): ")
    new_phone = input("New phone (or enter to skip): ")
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute(
            "UPDATE contacts SET name=%s WHERE name=%s",
            (new_name, name)
        )
    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE name=%s",
            (new_phone, name)
        )
    conn.commit()
    cur.close()
    conn.close()
    print("Updated")

# ---------- QUERY ----------
def search():
    print("1 - by name")
    print("2 - by phone prefix")
    ch = input()
    conn = connect()
    cur = conn.cursor()
    if ch == "1":
        name = input("Name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE name ILIKE %s",
            ('%' + name + '%',)
        )
    else:
        prefix = input("Prefix: ")
        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s",
            (prefix + '%',)
        )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

# ---------- DELETE ----------
def delete():
    print("1 - by name")
    print("2 - by phone")
    ch = input()
    conn = connect()
    cur = conn.cursor()
    if ch == "1":
        name = input("Name: ")
        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    else:
        phone = input("Phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")

# ---------- MENU ----------
def main():
    create_table()
    while True:
        print("\n1 CSV\n2 Add\n3 Update\n4 Search\n5 Delete\n6 Exit")
        ch = input("> ")
        if ch == "1":
            insert_csv()
        elif ch == "2":
            add_contact()
        elif ch == "3":
            update()
        elif ch == "4":
            search()
        elif ch == "5":
            delete()
        elif ch == "6":
            break
if __name__ == "__main__":
    main()