# Paralelismo-y-Concurrencia-
Programas y ejemplos de concurrencia, paralelismo y sincronización (Python, Java y C): hilos, procesos, condiciones de carrera, deadlock, starvation, semáforos y monitores.
## Contenido
### Concurrencia (hilos)
- Ejemplo concurrente con múltiples tareas (Python/Java/C).
- Condición de carrera con contador compartido y corrección con exclusión mutua.

### Paralelismo (procesos)
- Creación de procesos y sincronización (Python `multiprocessing`, Java `ProcessBuilder`, C `fork/waitpid`).

### Problemas de sincronización
- **Race condition** (contador compartido).
- **Deadlock** (adquisición de recursos en distinto orden) y corrección.
- **Starvation** (filósofos comensales) y corrección con monitor.

### Monitores (filósofos comensales)
- Monitor en Python con `Condition`.
- Monitor en Java con `synchronized` + `wait/notifyAll`.
- Equivalente en C con `pthread_mutex` + `pthread_cond`.
