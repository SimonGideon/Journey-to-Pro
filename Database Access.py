import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE use (name text, age integer)")
c.execute("SELECT * FROM user")
print(c.fetchall())
conn.close()


def dict_factory(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d
conn = sqlite3.connect(":memory:")
conn.row_factory = dict_factory


# Accessing MySQL database using MYSQLLdb
import MySQLdb
class Dbconnect(object):
    def __init__(self):
        self.dbconnection = MySQLdb.connect(host='host_example',
                                            prt=int('port_example'),
                                            user='user_example',
                                            password='pass_example',
                                            db='schema_example')
        self.dbcursor = slf.dbconnection.cursor()
    def commit_db(self):
        self.dbconnection.commit()
    def close_db(self):
        self.dbcursor.close()
        self.dbconnection.close()
db = Dbconnect()
db.dbcursor.execute('SELECT * FROM %s' % 'table_example'
# Connection.

import psycopg2
conn = psycopg2.connect(database="testpython",
                        user="postgres",
                        host="localhost",
                        password="abc13",
                        port="5432")
cur = conn.cursor()
cur.execute("""CREATE TABLE FRUITS (
                    id INT ,
                    fruit_name TEXT,
                    color TEXT,
                    price REAL
            )""")
conn.commit()
conn.close()



# Using sqlalchemy.
from sqlachemy import create_egine
from sqlalchem.engine.url import URL

url = URL(drivrname='mysql',
          usetname='user',
          password='passwd',
          host='host',
          database='db')
engine = create_egine(url)

# import pandas as pd
con = engine.connect()
dataframe = pd.read_sql(sql=query, con=con)


