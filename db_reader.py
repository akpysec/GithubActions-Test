import sqlite3

connection = sqlite3.connect('BITTREX_TICKER.sqlite')
cursor = connection.cursor()
sqlite_select_query = """SELECT * from BITTREX"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("DB Contents:")
for line in records:
    print(line)
connection.close()
