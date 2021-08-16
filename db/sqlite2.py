import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table lang (name, first_appeared)")

# this is the qmark style:
cur.execute("insert into lang values (?, ?)", ("C", 1972))

# The qmark style used with executemany()
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("insert into lang values (?, ?)", lang_list)

# And this is the named style:
cur.execute("select * from lang where first_appeared=:year", {"year": 1991})
print(cur.fetchall())

conn.close()
