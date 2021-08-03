import sqlite3

conn = sqlite3.connect('python/db/teste.db')

cur = conn.cursor()

choice = input('''
[1] - Create Items
[2] - Read Items
''')

if choice == '1':
    cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='stocks' ''')

    if cur.fetchone()[0]==0 : {
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
    }

    date = input('Date: ')
    trans = input("Trans: ")
    symbol = input('Symbol: ')
    qty = float(input('Qty: '))
    price = float(input('Price: '))

    # insert a row of data
    cur.execute(f"INSERT INTO stocks VALUES ('{date}', '{trans}', '{symbol}', {qty}, {price})")

elif choice == '2':
    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

else:
    print('Option not found!!')
# save the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
