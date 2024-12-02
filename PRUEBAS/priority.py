import heapq

def insertar(cola, elemento, prioridad):
    heapq.heappush(cola, (prioridad, elemento))

def extraer(cola):
    return heapq.heappop(cola)[1] if cola else None

# Ejemplo de uso
mi_cola = []
insertar(mi_cola, 'tarea1', 3)
insertar(mi_cola, 'tarea2', 1)
insertar(mi_cola, 'tarea3', 2)

print(extraer(mi_cola))  # Salida: tarea2
print(extraer(mi_cola))  # Salida: tarea3
print(extraer(mi_cola))  # Salida: tarea1
print(extraer(mi_cola))  # Salida: None (cola vacía)

