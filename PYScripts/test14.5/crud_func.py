import sqlite3
def initiate_db():

    connection = sqlite3.connect("prod_db.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
	    "id"	INTEGER,
	    "title"	TEXT NOT NULL,
	    "desc"	TEXT,
	    "price"	INTEGER NOT NULL,
	    PRIMARY KEY("id" AUTOINCREMENT)
        )
    	""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
	    "id"	INTEGER NOT NULL,
	    "username"	TEXT NOT NULL,
	    "email"	TEXT NOT NULL,
	    "age"	INTEGER NOT NULL,
	    "Balance"	INTEGER NOT NULL DEFAULT 1000,
	    PRIMARY KEY("id" AUTOINCREMENT)
        )
    	""")
    connection.commit()
    connection.close()

def get_all_prods():
    initiate_db()
    connection = sqlite3.connect("prod_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    result = cursor.fetchall()
    connection.close()
    return result

def add_user(username, email, age):
    connection = sqlite3.connect("prod_db.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username,email,age) VALUES (?,?,?)",
                   (f"{username}", f"{email}", age))
    connection.commit()
    connection.close()
def is_exists(username):
    connection = sqlite3.connect("prod_db.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM Users WHERE username = ?",(str(username),))
    result = cursor.fetchone()
    connection.close()
    if result[0] > 0:
        return True
    else:return False