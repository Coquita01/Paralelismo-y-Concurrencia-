import threading

contador = 0
lock = threading.Lock()  # Bloqueo para sincronización

def increment():
    global contador
    for _ in range(100000):
        with lock:  # Lock aplicado en sección crítica
            contador += 1

hilos = []
for _ in range(5):
    t = threading.Thread(target=increment)
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

print(f"Valor final del contador: {contador}")