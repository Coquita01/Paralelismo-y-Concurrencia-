import threading

contador = 0  # Recurso compartido

def increment():
    global contador
    for _ in range(100000):
        contador += 1

hilos = []
for _ in range(5):  # Crear 5 hilos
    t = threading.Thread(target=increment)
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

print(f"Valor final del contador: {contador}")