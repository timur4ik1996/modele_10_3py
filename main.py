import time
from threading import Thread, Lock
from random import randint


class Bank:

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        tr = 100
        for i in range(tr):
            random = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random
            print(f'Пополнение{random}. Баланс:{self.balance}''\n')
            time.sleep(0.001)

    def take(self):
        tr = 100
        for i in range(tr):
            random = randint(50, 500)
            print(f'Запрос на {random}''\n')
            if self.balance < random:
                print("Запрос отклонен недостаточно средста"'\n')
                self.lock.acquire()
            else:
                self.balance -= random
                print(f'Снятие : {random}.Баланс :{self.balance}''\n')
                time.sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
