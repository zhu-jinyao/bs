import _thread
from machine import utime

def testThread(num):
    while 1:
        print(num)
        utime.sleep(2)

def testThread2(num):
    while 1:
        print(num)
        utime.sleep(2)

a=1
b=2
_thread.start_new_thread(testThread, (a))#启动线程
_thread.start_new_thread(testThread2, (b))#启动线程