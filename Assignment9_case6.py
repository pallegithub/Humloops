import sqlite3 as ms 
try: 
    id=int(input("Enter ID:")) 
    sql = "SELECT * FROM products WHERE id=%d" 
    con = ms.connect("sample.db" ) 
    cursor=con.cursor() 
    cursor.execute(sql%(id,)) 
    row=cursor.fetchone() 
    if row is not None: 
        name=input("Enter product name: ") 
        price=int(input("Enter product price: "))
        sql="UPDATE products SET name='%s', price='%d' WHERE id='%d'" 
        cursor.execute(sql%(name,price,id)) 
        print("Record Updated Successfully") 
        con.commit() 
    else: 
        print("Not Existed") 
except ms.DatabaseError as e: 
    if con: 
        con.rollback() 
        print("There is a problem with sql",e) 
finally: 
    if cursor: 
        cursor.close() 
    if con: 
        con.close()