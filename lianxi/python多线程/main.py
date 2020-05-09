import _thread
import logging
import threading
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

# def loop0():
#     logging.info("start loop0 at "+ ctime())
#     sleep(4)
#     logging.info("end loop0 at "+ ctime())
#
# def loop1():
#     logging.info("start loop1 at "+ ctime())
#     sleep(2)
#     logging.info("end loop1 at "+ ctime())
#
# def main():
#     logging.info("start all at "+ ctime())
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1,())
#     sleep(6)
#     logging.info("end all at " + ctime())


loops = [2,4]

class MyThread(threading.Thread):
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop" + str(nloop) + "at "+ ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) +  "at "+ ctime())

def main():
    logging.info("start all at "+ ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()

#原语
##锁
##信号量


