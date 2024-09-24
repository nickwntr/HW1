import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
	"id"	INTEGER,
	"username"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"age"	INTEGER,
	"balance"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
""")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_mail ON Users (email)")
#for i in range(10):
#    cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)",(f"User{i+1}",f"example{i+1}@gmail.com", (i+1)*10 , 1000))
cursor.execute("DELETE FROM Users WHERE id = 6")
cursor.execute("UPDATE Users SET balance = 500 WHERE id%2 != 0")
cursor.execute("SELECT COUNT(*) FROM Users")
usernum = cursor.fetchone()
cursor.execute("SELECT SUM(balance) FROM Users")
totalsum = cursor.fetchone()
print(totalsum[0]/usernum[0])

connection.commit()
connection.close()
