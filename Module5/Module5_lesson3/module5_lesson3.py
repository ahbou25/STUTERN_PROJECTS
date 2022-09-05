import sqlite3
# print("imported successfully" )

#create a connection to a database
conn = sqlite3.connect("sales.db")
#print("connected successfully")

#create a cursor object
cursor = conn.cursor()
#print("cursor is connected successfully")

#Format to display output in a tabular form
items = cursor.fetchall()
print("item_ID" + "\t\tname" + "\t\t\tcost_price" + "\t\t\tquantity_in_stock" "\n" f"('.' * 80)")

#loop through the items
for item in items:
    item_ID, name, cost_price, quantity_in_stock = item
    # print(f"{item_ID}\t\t{name}\t\t\t{cost_price}\t\t\t{quantity_in_stock}")

#To calculate the amount the business owner invested in procuring the items
cursor.execute("SELECT SUM(cost_price) FROM inventory")
item = cursor.fetchall()
print("The amount the business owner invested in procuring the items is: ",item)

# To calculate the average quantity of items in stock
cursor.execute("SELECT AVG(quantity_in_stock) FROM inventory")
item = cursor.fetchall()
print("The item with the average quantity in stock is: ", item)

# To calculate the least quantity of items in stock
cursor.execute("SELECT name, MIN(quantity_in_stock) FROM inventory")
item = cursor.fetchall()
print("The item with the least quantity in stock is: ", item)

# To calculate the most quantity of items in stockcd
cursor.execute("SELECT name, MAX(quantity_in_stock) FROM inventory")
item = cursor.fetchall()
print("The item with the most quantity in stock is: ", item)

#commit the database and table
conn.commit()

#close the connection to database
conn.close()


