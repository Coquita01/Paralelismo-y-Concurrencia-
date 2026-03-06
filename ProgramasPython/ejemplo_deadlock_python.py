import threading
import time

scanner = threading.Lock()
blu_ray = threading.Lock()

def proceso_A():
    scanner.acquire()
    time.sleep(0.1)
    blu_ray.acquire()

    print("A usa scanner y blu-ray")

    blu_ray.release()
    scanner.release()

def proceso_B():
    blu_ray.acquire()
    time.sleep(0.1)
    scanner.acquire()

    print("B usa blu-ray y scanner")

    scanner.release()
    blu_ray.release()

t1 = threading.Thread(target=proceso_A)
t2 = threading.Thread(target=proceso_B)
t1.start(); t2.start()
t1.join(); t2.join()