from threading import Thread
from datetime import datetime
import time


def write_words(word_count, file_name):
    count = 0
    with open(file_name, 'w', encoding='utf-8') as my_file:
        for i in range(1, word_count + 1):
            count += 1
            my_file.write(f'Какое-то слово № {count}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
    return write_words


time_start_f = datetime.now()
func_1 = write_words(10, 'example1.txt')
func_2 = write_words(30, 'example2.txt')
func_3 = write_words(200, 'example3.txt')
func_4 = write_words(100, 'example4.txt')
time_end_f = datetime.now()
time_res_f = time_end_f - time_start_f
print(f'Работа потоков {time_res_f}')


time_start_thr = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_thr = datetime.now()
time_res_thr = time_end_thr - time_start_thr
print(f'Работа потоков {time_res_thr}')
