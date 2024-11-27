import threading
from threading import Thread, Lock
import random
import time

class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transaction = 100
        while transaction >= 0:
            transaction -= 1
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rand = random.randint(50,500)
            self.balance += rand
            time.sleep(0.001)
            print(f'Пополнение: {rand}. Баланс: {self.balance}')

    def take(self):
        transaction = 100
        while transaction >= 0:
            transaction -= 1
            rand = random.randint(50,500)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
