import sqlite3

#create a connection
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

#query all data
cursor.execute("SELECT * FROM events WHERE band='Tigers'")
rows = cursor.fetchall()
print(rows)

#query selected data
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.14'")
rows = cursor.fetchall()
print(rows)

#insert new data
new_rows = [('Cats', 'Cat City', '2088.10.17'), ('Dogs', 'Dog City', '2088.10.20'), ('Mice', 'Mouse City', '2088.10.29'), ('Birds', 'Bird City', '2088.10.12')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()



