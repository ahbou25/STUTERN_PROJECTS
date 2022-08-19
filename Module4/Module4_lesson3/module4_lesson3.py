import sqlite3
#print ('imported successfully')

# connect to a database
conn = sqlite3.connect('student_db')
# print('connected successfully')

#create a cursor object
cursor = conn.cursor()

#creating a new table
# cursor.execute(""" CREATE TABLE students_data( 
#             First TEXT
#             Last TEXT
#             Email TEXT
#             )

# """)
# print('table created successfully')            

#Inserting several values to table
Students_list = [('Usman','Olawale','usmanolawale@stutern.com'),
                 ('Ibrahim','Olarongbe','ibrahimolarongbe@stutern.com'),
                 ('Omolade','Nafisat','omoladenafisat@stutern.com')
                ]
# print ("Student list created successfully!")
cursor.executemany("INSERT INTO students_data VALUES (?, ?, ?)", Students_list)

#querying the database
cursor.execute("SELECT * FROM students data")
#print ("Query executed successfully!")

#format output to display in a tabular form
items =cursor.fetchall()
print("First" + "\t\tLast" + "\t\tEmail \n" f"{'.'* 60}")

#looping through the items
for item in items:
    First, Last, Email = item
    print(f"{First:16}{Last:16}{Email:30}")

# conn. commit ()
# print ("Committed successfully!")

#Alter table statement
#Change the table name

cursor.execute("ALTER TABLE students_data RENAME TO group_info")
# conn. commit()
# print ("Table renamed successfully!")

#Adding a new column
cursor.execute("ALTER Table group info ADD column Age")
# conn. commit()
print("New column added successfully!")

#Updating new column age with details
cursor.execute ("UPDATE group_info SET Age = '33'")
conn. commit()


