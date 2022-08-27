import sqlite3
import random
# This funcion inserts 50 random names and pays
def massCreate():
    conn=sqlite3.connect('employee.db')
    c=conn.cursor()
    last=("Johnson","smith","Williams","Brown","Jones","miller","Davis","Garcia","Rodriguez","wilson")
    first=("James","Mary","John","Robert","Jennifer","Patricia","Michael","Linda","David","Elizabeth","William","Barbara")
    
    for i in range(50):
        f=first[random.randrange(0,11)]
        l=last[random.randrange(0,9)]
        pay=random.randrange(20000,100000)
        c.execute("INSERT INTO employees(first,last,pay) VALUES (?,?,?)",(f,l,pay,)) 
        
    conn.commit()
    conn.close()    
print(random.randrange(1,10))
#massCreate()

conn=sqlite3.connect('employee.db')

c=conn.cursor()

#c.execute("""CREATE TABLE employees(
 #  id INTEGER PRIMARY KEY AUTOINCREMENT,    
  #  first text,
   #     last text,
    #  pay integer
     # )
      # """)

#c.execute("""CREATE TABLE sales(
 #  Saleid INTEGER PRIMARY KEY AUTOINCREMENT,    
  #  Item text,
   # price text,
    #salesPersonID integer
     # )
      # """)
f="bob"
l="smith"
pay=55000

#.execute("INSERT INTO sales(Item,price,salesPersonID) VALUES ('Towel','25',2)")
conn.commit()


c.execute("SELECT * from employees")
print(c.fetchall())
conn.commit()
conn.close()