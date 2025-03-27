import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user",
  database="nestdatabase"
)

mycursor = mydb.cursor()

########Database Creation########
#mycursor.execute("CREATE DATABASE nestdatabase")

#mycursor.execute("SHOW DATABASES") #Returns a list
########Database Creation########

########Table Creation########
def createTable():
    
    mycursor.execute("CREATE TABLE organizations (ID INT AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(255), path VARCHAR(255))")

    #mycursor.execute("ALTER TABLE characters ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
########Table Creation########

########Adding Characters########
def addCharacters():
    sql = "INSERT INTO characters (name, path) VALUES (%s, %s)"
    val = ("Shadow the Hedgehog", "img/chars/shadow_the_hedgehog.png") ##First the name, then the relative path.
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Row added! ID of last Row:", mycursor.lastrowid)
########Adding Characters########

########Edit Characters########
def updateCharacters():
    
    sql = "UPDATE characters SET path = 'img/chars/shadow_the_hedgehog.png' WHERE path = 'db/img/shadow_the_hedgehog.png'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "Row edited!") 
########Edit Characters########

########Read Characters########
def getCharacters():
    
    mycursor.execute("SELECT * FROM characters")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
    return myresult

def extractCharPath ():
    
    get_path = getCharacters()
    char_path = [x[1] for x in get_path] #Returns a list of all paths.

    return char_path

def specificPath (char_path):
    
    str_path = char_path[0] #Returns the first row´s path
    
    return str_path  
########Read Characters########





########Test########
#add = addCharacters()
#update = updateCharacters()

#get = getCharacters()
#print(type(get))

#all_paths = extractCharPath()
#print(all_paths)
#path = specificPath(all_paths)
#print(path)
########Test########
