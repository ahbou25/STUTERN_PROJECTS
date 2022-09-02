import sqlite3
print("sqlite3 imported successfully")

# connect to database
conn = sqlite3.connect("celebs.db")
print('connected successfully')

#Create a cursor object
cursor = conn.cursor()
print("cursor connected successfully")

# Create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS celebrity(
             Name TEXT,
             Genre TEXT,
             Num_albums INTEGER,
             Age INTEGER,
             Awards INTEGER,
             Years_in_industry INTEGER
             )
 """) 
print("Table created successfully")   

# Inserting values to the table
music_data_set = [
                    ('wizkid', 'afrobeat', '3', '33', '71', '13'),
                    ('Burnaboy', 'afrobeat', '6', '30', '42', '10'),
                    ('Davido', 'afrobeat', '4', '31', '60', '12'),
                    ('2face', 'afrobeat', '7', '40', '88', '18'),
                    ('Dbanj', 'afrobeat', '8', '37', '76', '15'),
                    ('Wasiu', 'fuji', '20', '52', '40', '30'),
                    ('KSA', 'fuji','23', '63', '34', '28'),
                    ('Pasuma', 'fuji', '17', '56', '19', '17'),
                    ('Adele', 'RnB', '22', '48', '78', '15'),
                    ('Beyonce', 'RnB', '25', '44', '92', '30'),
                    ('Rihanna', 'HipHop', '21', '48', '82', '28'),
                    ('Eminem', 'Rap', '12', '49', '56', '45'),
                    ('JayZ', 'Rap', '23', '56', '67', '40'),
                    ('NF', 'Rap', '6', '28', '44', '28'),
                    ('TheWeeknd', 'HipHop', '8', '37', '103', '14'),
                    ('Adekunlegold', 'afro-pop', '6', '34', '36', '8'),
                    ('Bigsean', 'Rap', '8', '33', '89', '13'),
                    ('Buju', 'afrobeats', '1', '26', '16', '3'),
                    ('Passenger', 'country', '18', '39', '30', '20'),
                    ('Drake', 'HipHop', '9', '38', '70', '15'),
                    ('Chrisbrown', 'pop', '12', '36', '86', '16')
                ]
print("music_data_set table created successfully!")

cursor.executemany("INSERT INTO celebrity VALUES (?, ?, ?, ?, ?, ?)", music_data_set)

#Querying the database
cursor.execute("SELECT * FROM celebrity")
print("Query executed successfully!")

#Format to display in Tabular form
items = cursor.fetchall()
print("Name" + "\t\t\tGenre" + "\t\tNum_albums" + "\t\tAge" + "\t\tAwards" + "Years_in_industry")
#print(items)

#Loop through the items
for item in items:
    Name, Genre, Num_albums, Age, Awards, Years_in_industry = item
    print(f"{Name:25}{Genre:10}{Num_albums:10}{Age:22}{Awards:18}{Years_in_industry:18}")

conn.commit()
print("committed successfully")    

# The Most Decorated celebrity
cursor.execute("""
SELECT NAME, MAX(Awards)
FROM celebrity
""")
item = cursor.fetchall()
print(item)

#The Oldest Celebrity
cursor.execute("""
SELECT NAME, MAX(Age)
FROM celebrity
""")
item = cursor.fetchall()
print(item)

#The celebrity with the longest years in the industry
cursor.execute("""
SELECT NAME, MAx(years_in_industry)
FROM celebrity
""")
item = cursor.fetchall()
print(item)

#The celebrity with the least number of albums
cursor.execute("""
SELECT NAME, MIN(Num_albums)
FROM celebrity
""")
item = cursor.fetchall()
print(item)

#The most popular genre of music amongst all celebrities
cursor.execute("""
SELECT MAX(Genre)
FROM celebrity
""")
item = cursor.fetchall()
print(item)

# Commit the database and table
conn.commit()

#Close the connectiion to the database
conn.close()
