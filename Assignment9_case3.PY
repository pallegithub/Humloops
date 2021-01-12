import sqlite3
connection = sqlite3.connect('sample.db')
c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS products (
             id INT,
             name VARCHAR(50),
             price INT)""")
c.execute("INSERT INTO products (id,name,price) VALUES (101,'product1',58)")
c.execute("INSERT INTO products (id,name,price) VALUES (102,'product2',88)")
c.execute("INSERT INTO products (id,name,price) VALUES (102,'product3',98)")
c.execute("INSERT INTO products (id,name,price) VALUES (102,'product4',128)")
connection.commit()
connection.close()