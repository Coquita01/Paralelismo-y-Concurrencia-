import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        # pensar
        time.sleep(random.uniform(0.1, 0.3))


        # tomar tenedores
        forks[left].acquire()
        forks[right].acquire()

        # comer
        print(f"Filósofo {i} está comiendo")
        time.sleep(random.uniform(0.1, 0.2))

        # soltar tenedores
        forks[right].release()
        forks[left].release()

threads = [threading.Thread(target=philosopher, args=(i,), daemon=True) for i in range(N)]
for t in threads:
    t.start()

time.sleep(5)
print("Fin de la simulación")