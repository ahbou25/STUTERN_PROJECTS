import sqlite3
#print("imported successfully")

#Connect to a database
conn = sqlite3.connect("sales.db")
print("connected successfully")

# Create a cursor object
cursor = conn.cursor()
print("cursor connected successfully")

#Create  a Table
cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(
              item_ID INTEGER,
              name TEXT,
              cost_price REAL,
              quantity_in_stock INTEGER
              )
""")
print("Table created successfully")

# Inserting several values to the table
stationeries = [('01', 'exercise_book', '200.0', '100'),
                ('02', 'eraser', '50.0', '200'),
                ('03', 'pencil', '30.0', '150'),
                ('04', 'sharpener', '250.0', '400'),
                ('05', 'Text_book', '200.0', '150'),
                ('06', 'Envelope', '25.0', '100'),
                ('07', 'cellotape', '40.0', '180'),
                ('08', 'biro', '50.0', '105'),
                ('09', 'marker', '300.0','160'),
                ('10', 'pen', '200.0', '145')
                ]
print("stationeries table created successfully")

cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", stationeries)

#Query the database
cursor.execute("SELECT * FROM inventory")
print("query executed successfully")
            
#format to display output in a tabular form
items = cursor.fetchall()
print("item_ID" + "\t\tname" + "\t\t\tcost_price" + "\t\t\tquantity_in_stock" "\n" f"{'.' * 85}")

#looping through items
for item in items:
    item_ID, name, cost_price, quantity_in_stock = item
    print(f"{item_ID}\t\t{name}\t\t\t{cost_price}\t\t\t{quantity_in_stock}")

cursor.execute("""SELECT * FROM inventory
WHERE quantity_in_stock < 2
ORDER BY cost_price DESC;
"""
)
item = cursor.fetchall()
print(item)

#commit the database and table
conn.commit()

#close the connection to the database
conn.close()