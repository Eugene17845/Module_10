import multiprocessing
from datetime import datetime


def read_info(name):
    _all_data = []
    with open(name) as file:
        while True:
            str = file.readline()
            _all_data.append(str)
            if not str:
                break



filenames = [f'./file {number}.txt' for number in range(1, 5)]
time1 = datetime.now()
for file in filenames:
    read_info(file)
time2 = datetime.now()
print(f'{time2 - time1} (линейный)')

if __name__ == '__main__':
    time3 = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    time4 = datetime.now()
    print(f'{time4 - time3} (мультипоточный)')