from threading import Thread
import time
from queue import Queue
from random import randint


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

    def __repr__(self) -> str:
        return f'Table({self.number})'


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return f'Guest({self.name})'

    def run(self):
        time.sleep(randint(3, 5))



class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            is_sitting = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest} сел(-а) за стол номер {table}')
                    guest.start()
                    is_sitting = True
                    break
            if not is_sitting:
                self.queue.put(guest)
                print(f'{guest} в очереди')


    def discuss_guests(self):
        while not self.queue.empty() and any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table}')
                    table.guest.start()


tables = [Table(number) for number in range(1, 6)]
cafe = Cafe(*tables)
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe.guest_arrival(*guests)
cafe.discuss_guests()