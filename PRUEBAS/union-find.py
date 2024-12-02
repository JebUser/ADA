class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def findrank(self, x):
        return self.rank[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1


# Crear un conjunto disjunto con 6 elementos (0 al 5)
disjoint_set = DisjointSet(6)

# Función para imprimir el estado actual del conjunto disjunto
def print_disjoint_set():
    print("Conjunto Disjunto:")
    for i in range(6):
        print(f"Elemento {i}: Raíz = {disjoint_set.find(i)} \n Rango = {disjoint_set.findrank(i)}")

# Imprimir el conjunto disjunto inicial
print("Estado Inicial:")
print_disjoint_set()
print()

# Unir algunos conjuntos
disjoint_set.union(0, 1)
disjoint_set.union(2, 3)
disjoint_set.union(4, 5)

# Imprimir el conjunto disjunto después de las uniones
print("Después de las Uniones:")
print_disjoint_set()
print()

# Realizar búsquedas en algunos elementos
print("Operaciones de Búsqueda:")
print("Búsqueda de 0:", disjoint_set.find(0))
print("Búsqueda de 3:", disjoint_set.find(3))
print("Búsqueda de 5:", disjoint_set.find(5))


# Realizar una unión más
disjoint_set.union(1, 3)

# Imprimir el conjunto disjunto después de la última unión
print("Después de la Última Unión:")
print_disjoint_set()
