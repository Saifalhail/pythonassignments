import mysql.connector
import pandas as pd

# 15)
# Create Database
# conn = mysql.connector.connect(user='root', password='Yucme00.', host='127.0.0.1')
# cursor = conn.cursor()
# cursor.execute("DROP database IF EXISTS studentInfo")
# sql = "CREATE database studentInfo"
# cursor.execute(sql)

# Retrieving List of Databases
# print("List of databases: ")
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

#Closing the connection
# conn.close()

# Connect to Database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Yucme00.",
#   database="studentInfo"
# )

# mycursor = mydb.cursor()

# Create Table
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), course VARCHAR(255), institute VARCHAR(255), fees VARCHAR(255))")
# Create DF for student info
data = [['Name', 'Tim'], ['Course', 'Science'], ['Institute', 'Research'], ['Fees', 150]]
df = pd.DataFrame(data, columns = ['Key', 'Value'])
# print (df)
# df.to_sql(con=mydb, name='studentInfo', if_exists='replace')

try:
    mydb = mysql.connector.connect(host="localhost", database = 'studentInfo',user="root", passwd="Yucme00.",use_pure=True)
    query = "Select * from students;"
    result_dataFrame = pd.read_sql(query,mydb)
    # mydb.close() #close the connection
except Exception as e:
    # mydb.close()
    print(str(e))

result_dataFrame = pd.read_sql(query, mydb)
print (result_dataFrame)