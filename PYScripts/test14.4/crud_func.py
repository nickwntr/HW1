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