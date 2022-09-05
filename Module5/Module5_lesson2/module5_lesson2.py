from importlib.resources import contents
import sqlite3
print("imported successfully")

import csv
print("printed successfully")

#connect to a database
conn = sqlite3.connect("WAEC_Scores.db")
print("cursor connected successfully")

#create cursor object
cursor = conn.cursor()
print("cursor connected succcessfully")

#Create WAEC_score table

table = ("""CREATE TABLE IF NOT EXISTS waec_scores(
            ID INTEGER,
            Name TEXT,
            Maths INTEGER,
            English INTEGER,
            Literature INTEGER,
            Commerce INTEGER,
            Agriculture INTEGER,
            Government INTEGER,
            Biology INTEGER,
            Statistics INTEGER,
            Accounting INTEGER
            )
""")       

print("table created successfully")

cursor.execute(table)

with open('Module5\WAEC_Scores.csv', "r") as opened_file:
    read_file = csv.reader(opened_file)
    next(read_file)


#To insert values of the read_file into the sql table
    cursor.executemany("""
                      INSERT INTO waec_scores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                      """, read_file)
#print("created successfully")

#querying the database
cursor.execute("SELECT * FROM waec_scores")                       
#print("queried successfully")

#format to display output in tabular form
items = cursor.fetchall()

print("ID" + "\tNAME" + "\Maths" + "\tEnglish" + "\tLiterature" + "\tCommerce" + "\tAgriculture" + "\tGovernment" + "\tBiology" + "\tStatistics" + "\tAccounting")


# loop through the items
for item in items:
    ID, Name, Maths, English, Literature, Commerce, Agriculture, Government, Biology, Statistics, Accounting = items
    print(item)

#Student with the highest score in maths
def highest_in_maths():
    cursor.execute("""
    SELECT Name, MAX(Maths) FROM waec_scores
    """)
    item = cursor.fetchall()
    print(f"highest score in math, {item}")
    highest_in_maths()

#Student with lowest score in English
def lowest_in_english():
    cursor.execute("""
    SELECT Name, MIN(English) FROM waec_scores
    """)
    item = cursor.fetchall()
    print(f"lowest score in english, {item}") 
    lowest_in_english()  

#AVERAGE score of students in maths
def average_in_maths():
    cursor.execute("""
    SELECT AVG(Maths) FROM waec_scores
    """)
    item = cursor.fetchall()
    print(f"average_in_maths {item}") 
    average_in_maths()  

#AVERAGE score of students in English
def average_in_english():
    cursor.execute("""
    SELECT AVG(English) FROM waec_scores
    """)
    item = cursor.fetchall()
    print(f"average_in_english {item}") 
    average_in_english()  

#The best performing student
def overall_best():
    cursor.execute("""SELECT Name, 
                   FROM(
                   SELECT Name, SUM(Maths + English + Literature + Commerce + Agriculture + Government + Biology + Statistics + Accounting)
                   FROM waec_scores
                   GROUP BY Name)
                   """)
    item = cursor.fetchall()
    print(f"overall best student {item}") 
    overall_best() 

#The best average scores
def best_average_scores():
    cursor.execute("""SELECT Name, 
                   FROM(
                   SELECT Name, AVG(Maths + English + Literature + Commerce + Agriculture + Government + Biology + Statistics + Accounting)
                   FROM waec_scores
                   GROUP BY Name)
                   """)
    item = cursor.fetchall()
    print(f"best_average_scores, {item}") 
    overall_best() 

#commit the database and table
conn.commit()
   
#close the connection
conn.close()