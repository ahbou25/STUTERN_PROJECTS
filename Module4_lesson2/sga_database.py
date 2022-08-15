import sqlite3

print("successful")

#connect to database
conn = sqlite3.connect("SGA_1_3_learners.db")

print("connection created successfully")

# #create cursor
cursor = conn.cursor()

print("cursor created sucessfully")

# create stuttern_students table
# cursor.execute(

#     """
#     CREATE TABLE IF NOT EXISTS stuttern__students (
#             first_name text,
#             last_name text,
#             email_address text,
#             course text
#     )""")

# print("table created sucessfully")

#INSERT INTO STATEMENT
# cursor.execute(INSERT INTO stutern_student)
#conn.commit()

#conn.close()

all_students = [
                    ('Abubakar', 'Adisa', 'adisaabubakar@gmail.com', 'Data Science'),
                    ('Adebisi', 'Afolabi', 'wasola.afolabi@yahoo.com', 'Data Science'),
                    ('Adedoyin', 'Abass', 'doyinabass0@gmail.com', 'Data Science'),
                    ('Awonaike', 'Tawakalitu', 'purpleduralumin@gmail.com', 'Data Science'),
                    ('Babajide', 'Adesugba', 'jide_ade@hotmail.com', 'Data Science'),
                    ('Bukola', 'Ajayi',	'bukolam.ajayi@gmail.com', 'Data Science'),
                    ('Binta', 'Umar', 'ubinta63@yahoo.com', 'Data Science'),
                    ('Christian', 'Uzondu',	'uzonduchristian2@gmail.com', 'Data Science'),
                    ('Cynthia', 'Awiya', 'awiyac@yahoo.com', 'Data Science'),
                    ('Deborah', 'Olorunnishola', 'deboraholuwatobi247@gmail.com', 'Data Science'),
                    ('Eke', 'Ihuoma', 'ihuomaeke28@gmail.com', 'Data Science'),
                    ('Esther', 'Akpanowo', 'estherakpanowo@gmail.com', 'Data Science'),
                    ('Eniola', 'Osadare', 'dorcasosadare@gmail.com', 'Data Science'),
                    ('Etariemi', 'Louis', 'etariemilouis@gmail.com', 'Data Science'),
                    ('Faith', 'Amure', 'amuretalodabif@gmail.com', 'Data Science'),
                    ('Ganiyat', 'Shittu', 'ganiyatas@gmail.com', 'Data Science'),
                    ('Gideon', 'Uko', 'ukogideon13@gmail.com', 'Data Science'),
                    ('Idowu', 'Adesanya', 'idsworld22@yahoo.com', 'Data Science'),
                    ('Joyce', 'Ezeonwu', 'joyceokore@gmail.com', 'Data Science'),
                    ('Kehinde', 'Orolade', 'kehindeorolade@gmail.com', 'Data Science'),
                    ('Kafayat', 'Ibrahim', 'kafayatadenike10@gmail.com', 'Data Science'),
                    ('Lawrence', 'Aneshimokha', 'anelawrence1@gmail.com', 'Data Science'),
                    ('Mariam', 'Adeoti', 'adetutuadebola28@gmail.com', 'Data Science'),
                    ('Ogechi', 'Njemanze', 'ogenjemz@gmail.com', 'Data Science'),
                    ('Omowunmi', 'Awoniran',	'mowunmi11@gmail.com', 'Data Science'),
                    ('Placidus', 'Ali',	'Placidusali@gmail.com', 'Data Science'),
                    ('Praise', 'Emmanuel', 	'praiseemmanuel9ic@gmail.com', 'Data Science'),
                    ('Prince', 'Ekeocha',	'prince.ekeocha@gmail.com', 'Data Science'),
                    ('Rasheedat', 'Sikiru',	'rasheedatsikiru@gmail.com', 'Data Science'),
                    ('Ramotallah', 'Jubril', 'jubrilramotallah03@gmail.com', 'Data Science'),
                    ('Sheriiff', 'Azeez',	'SheriffOlaitan71@gmail.com', 'Data Science'),
                    ('Stephen', 'Ogungbile', 'stephenfunso@gmail.com', 'Data Science'),
                    ('Temitope', 'Bamidele', 'bamideletemitope42@gmail.com', 'Data Science'),
                    ('Theresa', 'Karamor',	'teriekarie@gmail.com', 'Data Science'),
                    ('Tina', 'Uyateide',	'tinauyats@gmail.com', 'Data Science'),
                    ('Victoria', 'Chukwuno',	'chukwunovictoria@gmail.com', 'Data Science')
                ]

cursor.executemany(
"""
INSERT INTO stuttern__students(first_name, last_name, email_address, course) 
VALUES (?,?,?,?)
""",

all_students

)

print("all students created successfully")

cursor.execute(
    """
    SELECT * from stuttern__students
    """

)

print("query executed successfully")

# Query the data

items = cursor.fetchall()
#format to display table
#print("first_name"+ "\t\t last_name"+ "\t\t email_address"+ "\t\t\t\t  course\n" f"{'.' * 100}")
print(cursor.fetchall())
print("first_name"+ "\t\t last_name"+ "\t\t email_address"+ "\t\t\t\t  course\n" f"{'.' * 120}")

#loop through items
for item in items:
    first_name, last_name, email_address, course = item
    print(f"{first_name:16}{last_name:16}\t\t{email_address}\t\t\t\t{course}")

#conn.commit()

conn.close()






  
