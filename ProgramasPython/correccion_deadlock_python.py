import threading
import time

# Semáforos binarios (solo un hilo puede usar el recurso a la vez)
scanner = threading.Semaphore(1)
blu_ray = threading.Semaphore(1)

def usar_recursos(nombre):
    # Regla de prevención: todos adquieren en el mismo orden
    scanner.acquire()
    try:
        time.sleep(0.1)
        blu_ray.acquire()
        try:
            time.sleep(0.1)
            print(f"{nombre} usa scanner y blu-ray")
        finally:
            blu_ray.release()
    finally:
        scanner.release()

t1 = threading.Thread(target=usar_recursos, args=("Proceso A",))
t2 = threading.Thread(target=usar_recursos, args=("Proceso B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Finalizó el proceso principal")