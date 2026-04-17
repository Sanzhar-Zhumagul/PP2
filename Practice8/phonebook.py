from connect import connect

def search(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    print(cur.fetchall())
    conn.close()

def add_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()
    conn.close()

def delete_user(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()
    conn.close()

def paginate(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    print(cur.fetchall())
    conn.close()

'''
# test
search("San")
add_user("Sanzhar", "+77001234567")
paginate(5, 0)
delete_user("Sanzhar")
'''