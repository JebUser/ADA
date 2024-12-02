"""
Nombre: Juan Esteban Becerra
Código: 8965694
"""
from sys import stdin



def main():
    toDest = float(stdin.readline())
    while toDest >= 0:
        vals = stdin.readline().split()
        tank, consume, costRefueld, nstations = float(vals[0]), float(vals[1]), float(vals[2]), int(vals[3])
        stations = []
        for i in range(nstations):
            toGas, priceC = map(float, stdin.readline().strip().split())
            stations.append((toGas, priceC))
        toDest = float(stdin.readline())

main()