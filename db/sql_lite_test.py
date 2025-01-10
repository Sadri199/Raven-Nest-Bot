import sqlite3

con = sqlite3.connect("ravenNest.db")  #Name of the file

cur = con.cursor()

#cur.execute("CREATE TABLE locations (Name, Picture)") #Name of the table to create

#cur.execute(""" 
#            INSERT INTO characters VALUES #the third part is the name of the Table
#           ("Goku", "/img/1.png")
#            """)
#con.commit() #Always have to commit so the data is saved inside the DB, if not, nothing happens

res = cur.execute("SELECT Name FROM characters") #Second is the name of the column, fourth is the name of the table.
test = res.fetchall() #How you access the DB.

print(test)