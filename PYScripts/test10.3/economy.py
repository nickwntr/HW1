import random
import time
from threading import Lock
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            dep = random.randint(50,500)
            self.balance += dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {dep}. Баланс: {self.balance} \n")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            wdraw = random.randint(50,500)
            print(f"Запрос на снятие {wdraw} \n")
            if self.balance >= wdraw:
                self.balance -= wdraw
                print(f"Снятие: {wdraw}. Баланс: {self.balance} \n")
            else:
                print("Запрос отклонен. Недостаточно средств \n")
                self.lock.acquire()
            time.sleep(0.001)