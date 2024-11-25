import threading
from datetime import datetime
import time
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()

res = time_stop - time_start
print(f'Работа потоков {res}')

time_start_1 = datetime.now()
thread = threading.Thread(target=write_words, args = (10, 'example5.txt'))
thread1 = threading.Thread(target=write_words, args = (30, 'example6.txt'))
thread2 = threading.Thread(target=write_words, args = (200, 'example7.txt'))
thread3 = threading.Thread(target=write_words, args = (100, 'example8.txt'))

thread.start()
thread1.start()
thread2.start()
thread3.start()

thread.join()
thread1.join()
thread2.join()
thread3.join()
time_stop_1 = datetime.now()

res_1 = time_stop_1 - time_start_1
print(f'Работа потоков {res_1}')
