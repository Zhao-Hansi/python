import multiprocessing
import random
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep, time


def download_task(file_name):
    print("开始下载任务，进程号是[%d]." % getpid())
    print("开始下载 %s" % file_name)
    download_time = random.randint(5, 10)
    sleep(download_time)
    print("%s 下载完成" % file_name)


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
