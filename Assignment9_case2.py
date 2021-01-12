import sqlite3
connection = sqlite3.connect('sample.db')
c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS products (
             id INT,
             name VARCHAR(50),
             price INT)""")
connection.commit()
connection.close()