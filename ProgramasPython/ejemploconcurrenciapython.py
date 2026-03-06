import time
import threading

def codificar():
    time.sleep(2)
    print("Codificando")

def responder_correos():
    time.sleep(2)
    print("Respondiendo correos")

def realizar_calculos():
    time.sleep(2)
    print("Realizar los calculos")

# Crear hilos (guardar referencias)
t1 = threading.Thread(target=codificar)
t2 = threading.Thread(target=responder_correos)
t3 = threading.Thread(target=realizar_calculos)

# Iniciar hilos
t1.start()
t2.start()
t3.start()

# Esperar a que terminen
t1.join()
t2.join()
t3.join()

print("Todas las tareas terminaron")