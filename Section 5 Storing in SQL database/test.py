import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


user = (1,'Arne','adc123')
users = [
    (2,'Rutger','rutger123'),
    (3,'Maarten','maarten123')
]

insert_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(insert_query,user)
cursor.executemany(insert_query,users)

#retreive data

select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
