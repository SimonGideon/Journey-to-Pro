import sqlite3
conn = sqlite3.connect('Database1.db')
c = conn.cursor()
# Create a table
c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')

# Insert a raw of data.
c.execute("INSERT INTO stock VALUES ('2006-01-05','BUY','RHAT',100,35,14)")
conn.commit()

conn.close()

# Getting Values from the db and error handling.
import sqlite3
conn = sqlite3.connect('Database1.db')
c = conn.cursor()
c.execute("SELECT * from table_name where id=cust_id")
for row in c:
    print(row)
# To fetch mathching.

print(c.fetchone())
# For mutiple row.
a=c.fetchall()
for row in a:
    print(row)

try:
except sqlite3.Error as e:
    print("An error occured:", e.args[0])