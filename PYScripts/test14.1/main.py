import sqlite3
from symtable import Class

from sqlalchemy import create_engine, Column, Select
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import column, Integer, String
engine = create_engine("sqlite:///not_telegram.db",echo=True)
Session = sessionmaker(bind=engine)

start = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users"

    ID = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    age = Column(Integer)
    balance = Column(Integer)


for u in start.query(User).all():
    print(u.__dict__)

with engine.connect() as conn:
    for row in conn.execute(Select(User.__table__)):
        print(row)
#connection = sqlite3.connect("not_telegram.db")
#cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Users(
# 	"id"	INTEGER,
# 	"username"	TEXT NOT NULL,
# 	"email"	TEXT NOT NULL,
# 	"age"	INTEGER,
# 	"balance"	INTEGER NOT NULL,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# )
# """)
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_mail ON Users (email)")
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)",(f"User{i+1}",f"example{i+1}@gmail.com", (i+1)*10 , 1000))
# cursor.execute("UPDATE Users SET balance = 500 WHERE id%2 != 0")
# cursor.execute("DELETE FROM Users WHERE id%3 = 1")
# cursor.execute("SELECT * FROM Users WHERE age != 60")
# users = cursor.fetchall()

# print(users)
# for user in users:
#     print(f"Имя:{user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]} ")

# connection.commit()
# connection.close()
