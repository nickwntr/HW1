import random
from threading import Thread
import time
import queue


class Table:
    def __init__(self,num):
        self.number = num
        self.guest = None

class Guest(Thread):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.quene = queue.Queue()

    def check_tables(self):
        result = False
        for table in self.tables:
            if table.guest != None:
                result = True

    def guest_arrival(self,*guests):
        for guest in guests:
            no_tables = False
            for table in self.tables:
                if table.guest == None:
                    print(f"Клиента {guest.name} посадили за стол {table.number}")
                    table.guest = guest
                    no_tables = True
                    table.guest.start()
                    break
            if not no_tables:
                print(f"Клиент {guest.name} стоит в очереди")
                self.quene.put(guest)



    def discuss_guests(self):
        while not self.quene.empty() or self.check_tables():
            for table in self.tables:
                if not table.guest.is_alive():
                    print(f"{table.guest.name} ушел. Стол {table.number} свободен")
                    table.guest = None
                    if not self.quene.empty():
                        table.guest = self.quene.get()
                        print(f"Клиента {table.guest.name} посадили за стол {table.number}")
                        table.guest.start()
        print("Клиентов Нет. День окончен")

