import sqlite3

conn = sqlite3.connect('./db/teste.db')

cur = conn.cursor()

# create table
cur.execute('''
            CREATE TABLE stocks (
                date text,
                trans text,
                symbol text,
                qty real,
                price real
            )
        ''')

# insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

# save the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
