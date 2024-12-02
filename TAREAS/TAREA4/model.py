"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 
"""
from sys import stdin


def main():
    n,m = map(int, stdin.readline().strip().split())
    while n != 0 or m != 0:
        aristas = []
        for i in range(m):
            u,v,w = map(int, stdin.readline().strip().split())
            aristas.append([u,v,w])
        if n-1 > m:
            print(-1)
        else:
            span(aristas,n)
        n,m = map(int, stdin.readline().strip().split())

main()