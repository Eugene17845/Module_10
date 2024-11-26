import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.run()

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        dey = 0
        while enemies > 0:
            enemies = enemies - self.power
            dey += 1
            time.sleep(1)
            print(f'{self.name} сражается {dey}, осталось {enemies} воинов.\n')
            if enemies == 0:
                print(f'{self.name} одержал победу спустя {dey} дней(дня)!')


first_knight = threading.Thread(target=Knight, args=('Sir Lancelot', 10))
first_knight.start()
second_knight = threading.Thread(target=Knight, args=("Sir Galahad", 20))
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')