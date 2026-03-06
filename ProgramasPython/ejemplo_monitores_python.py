import threading
import time
import random

N = 5
THINKING, HUNGRY, EATING = 0, 1, 2

class MesaMonitor:
    def __init__(self, n):
        self.n = n
        self.state = [THINKING] * n
        self.cond = threading.Condition()  # monitor

    def left(self, i):
        return (i + self.n - 1) % self.n

    def right(self, i):
        return (i + 1) % self.n

    def tomar_tenedores(self, i):
        with self.cond:  # entra al monitor (exclusión mutua)
            self.state[i] = HUNGRY
            # Espera hasta que ambos vecinos NO estén comiendo
            while self.state[self.left(i)] == EATING or self.state[self.right(i)] == EATING:
                self.cond.wait()  # libera el monitor y se bloquea
            self.state[i] = EATING  # ya puede comer

    def soltar_tenedores(self, i):
        with self.cond:  # entra al monitor (exclusión mutua)
            self.state[i] = THINKING
            self.cond.notify_all()  # despierta a los que esperan para reevaluar
def philosopher(i, mesa: MesaMonitor):
    while True:
        # pensar
        time.sleep(random.uniform(0.1, 0.3))

        # solicitar permiso al monitor para tomar ambos tenedores
        mesa.tomar_tenedores(i)

        # comer
        print(f"Filósofo {i} está comiendo")
        time.sleep(random.uniform(0.1, 0.2))

        # devolver tenedores y notificar
        mesa.soltar_tenedores(i)

mesa = MesaMonitor(N)

threads = [threading.Thread(target=philosopher, args=(i, mesa), daemon=True) for i in range(N)]
for t in threads:
    t.start()

time.sleep(5)
print("Fin de la simulación")