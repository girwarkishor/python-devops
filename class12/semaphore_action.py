from threading import Semaphore, Thread
import time


sem_obj = Semaphore(2)


def func_lazy(n):

    sem_obj.acquire()
    time.sleep(int(n))
    string_output = f"sleep completed with time {str(n)}"
    print(string_output)

    sem_obj.release()
    return string_output


t1 = Thread(target=func_lazy, args=('10', ))
t2 = Thread(target=func_lazy, args=('2'))
t3 = Thread(target=func_lazy, args=('1'))
t4 = Thread(target=func_lazy, args=('6'))

t1.start()
t2.start()
t3.start()
t4.start()


# assignment write an example using semaphore and multiprocessing



