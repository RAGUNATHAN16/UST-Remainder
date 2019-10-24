import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="remainder"
)

mycursor = mydb.cursor()


def printfun(res):
  for x in res:
    print(x)


def insert():
  name=input("Enter the reminder Name:")
  date=input("Enter the reminder Date in the format (YYYY.MM.DD):")
  details=input("Enter the reminder Details:")
  mySql_insert_query = """INSERT INTO `remainder_details`(`Name`, `Date`, `Details`) VALUES (%s, %s, %s) """
  recordTuple = (name, date, details)
  sc=mycursor.execute(mySql_insert_query, recordTuple)
  if sc!=1:
    print("Successfully Inserted:")
  else:
    print("Not Inserted")
    return
  viewall()
  
def update():
  viewall()
  idv=int(input("Enter the ID to be Updated:"))
  name=input("Enter the reminder Name to update:")
  date=input("Enter the reminder Date in the format (YYYY.MM.DD) to update:")
  details=input("Enter the reminder Details to update:")
  query = """ UPDATE remainder_details SET Name = %s , Date = %s , Details = %s WHERE id = %s """
  data = (name,date,details,idv)
  sc=mycursor.execute(query,data)
  if sc!=1:
    print(" Succesfully Updated")
  else:
    print("Not Updated")
    return
  viewall()
  
def delete():
  viewall()
  idv=int(input("Enter the ID to be Deleted:"))
  sql = """DELETE FROM remainder_details WHERE ID = %s"""
  sc=mycursor.execute(sql,(idv,))
  if sc!=1:
    print(" Successfully Deleted")
  else:
    print("Not Deleted")
    return
  viewall()
  


def viewall():
  print("(id,Name,Date,Details)")
  mycursor.execute("SELECT * FROM remainder_details")
  printfun(mycursor.fetchall())


while(1):

  print("Enter your choice \n 1. Insert a Reminder \n 2. View all Reminders \n 3. Update a Reminder \n 4. Delete a Reminder \n 5. Exit \n")

  n=int(input())

  if n==1:
    insert()
  elif n==2:
    viewall()
  elif n==3:
    update()
  elif n==4:
    delete()
  elif n==5:
    break
  
