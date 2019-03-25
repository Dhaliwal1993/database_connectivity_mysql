import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","mydb" )

if db:
    print("connection established")
else:
    print("connection failed")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#create table
cursor.execute("create table customers (name varchar(255),address varchar(255))")

#showing if any table exists
cursor.execute("show tables")
for x in cursor:
    print(x)

#inserting into table
sql="insert into customers(name,address)values(%s,%s)"
val=("Gursimrat","Vikas Nagar Ludhiana")
cursor.execute(sql,val)
db.commit()

sql="insert into customers(name,address)values(%s,%s)"
val=("Gursharan","Model Town Ludhiana")
cursor.execute(sql,val)
db.commit()

#select command
cursor.execute("SELECT * FROM customers")
myresult = cursor.fetchall()
for x in myresult:
  print(x)

#We use the fetchall() method, which fetches all rows from the last executed statement.
cursor.execute("SELECT * FROM customers")
myresult = cursor.fetchone()
print(myresult)

#select with where condition
cursor.execute("select name from customers where address='vikas nagar ludhiana'")
myresult=cursor.fetchone()
for x in myresult:
    print("Name: "+x)

#wildcard characters like
cursor.execute("select name from customers where address LIKE '%ludhiana%'")
myresult=cursor.fetchall()
for x in myresult:
    print(x)

# Prevent SQL Injection
    sql="select name from customers where address='%s'"
    adr=("Nagar")
    cursor.execute(sql,adr)
    myresult=cursor.fetchall()
    for i in myresult:
        print(i)

#limit keyword in python mysql
cursor.execute("select * from customers LIMIT 1")
myresult=cursor.fetchall()
for x in myresult:
    print (x)

#offset and this keyword to used to select records with limit of 1 but should start from record 2
cursor.execute("select * from customers LIMIT 1 offset 2")
myresult=cursor.fetchall()
for x in myresult:
    print (x)

#update command
cursor.execute("update customers set address='Jalandhar' where name='Gursharan'")
myresult=cursor.fetchall()
for x in myresult:
    print (x)

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()