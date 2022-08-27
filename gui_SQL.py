from tkinter import *
import sqlite3
import tkinter
import tkinter.messagebox
import pandas as pd

def commit():
    #makes sure all feilds are filled and if not A message box will pop up
   if(fnamebox.get("1.0","end-1c")=="" or lnamebox.get("1.0","end-1c")=="" or paybox.get("1.0","end-1c")==""):
      messagebox.showinfo(message="One or more feilds is empty")
   else:
       conn=sqlite3.connect('employee.db')
       c=conn.cursor()
       c.execute("INSERT INTO employees(first,last,pay) VALUES (?,?,?)",(fnamebox.get("1.0","end-1c"),lnamebox.get("1.0","end-1c"),paybox.get("1.0","end-1c")))
       conn.commit()
       conn.close()
       fnamebox.delete('1.0',END)
       lnamebox.delete('1.0',END)
       paybox.delete('1.0',END)
       messagebox.showinfo(message="Employee inserted")
def selectAll():
   sbox.delete('1.0',END)
   conn=sqlite3.connect('employee.db')
   c=conn.cursor()
   c.execute("Select * FROM employees")
   x=c.fetchall()
   #create a pandas dataframe with all rows of the table to make the output more orginized
   df=pd.DataFrame(x,columns=("id","first","last","pay"))
   df.set_index('id',inplace=True)
   sbox.insert(END, df)
   
   conn.commit()
   conn.close()
def delByID():
 
  
    #makes sure the ID feild is filled and if not A message box will pop up
   if(delbox.get(1.0,"end-1c")==""):
       messagebox.showinfo(message="ID Feild is empty")
   else:
       x=delbox.get(1.0,"end-1c")
       conn=sqlite3.connect('employee.db')
       c=conn.cursor()
       c.execute("Select * FROM employees WHERE id=?",(x,))
       y=c.fetchone()
       print(y)
       #checks to see if id is in table and if not the user will be notified
       if(y!=None):
          
           x=delbox.get(1.0,"end-1c")
           c.execute("DELETE FROM employees WHERE id=?",(x,))
           messagebox.showinfo(message="employee with ID: "+ str(delbox.get(1.0,"end-1c")) + " has been removed")
       else:
          messagebox.showinfo(message="ID is not in the table")
         
       conn.commit()
       conn.close()
    

window = Tk()
# set window title
window.title("Employee Table editor")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg='lightgray')
var=StringVar()
first=Label(window, textvariable=var)
var.set("first")
first.pack()
fnamebox=Text(window, height = 1,
                width = 25,
                bg = "light yellow")
fnamebox.pack()

var=StringVar()
last=Label(window, textvariable=var)
var.set("last")
last.pack()
lnamebox=Text(window, height = 1,
                width = 25,
                bg = "light yellow")
lnamebox.pack()

var=StringVar()
pay=Label(window, textvariable=var)
var.set("pay")
pay.pack()
paybox=Text(window, height = 1,
                width = 25,
                bg = "light yellow")
paybox.pack()



b=Button(window,text="add", command=commit)
b.pack()
sbox=Text(window, height = 10,
                width = 40,
                bg = "light gray"
                )
sbox.pack()
sb=Button(window,text="List All Employees", command=selectAll)
sb.pack()

var=StringVar()
delete=Label(window, textvariable=var)
var.set("Delete By ID")
delete.pack()
delbox=Text(window, height = 1,
                width = 25,
                bg = "light yellow")
delbox.pack()
db=Button(window,text="Delete", command=delByID)
db.pack()
#Runs SelectAll when opened so the user will see all employees upon opening
selectAll()
window.mainloop()


