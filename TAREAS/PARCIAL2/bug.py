"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 1216
"""

from sys import stdin
import math

#operaciones disjoint set union
#**************************************

def makeSet(v):
    p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)

    if u != v:
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1

#****************************************

def kruskal(aristas,n):
    global p, rango
    pesos = []
    connected = 0
    p, rango = [0 for _ in range(1000000)], [0 for _ in range(1000000)]

    for i in range(n):
        makeSet(i)
    i = 0
    while i != len(aristas) and connected != n-1:
        u,v = aristas[i][0],aristas[i][1]

        if findSet(u) != findSet(v):
            unionSet(u,v)
            connected +=1
            pesos.append(aristas[i][2])
        i+=1

    return pesos

def solve(points,n):
    ans = 0
    m = len(points)
    edges = []

    for i in range(m):
        for j in range(i + 1, m):
            x1, y1 = points[i]
            x2, y2 = points[j]
            weight = math.ceil(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            edges.append((i, j, weight))

    edges.sort(key = lambda x: x[2])
    ans = kruskal(edges, len(edges))
    ans.sort()
    return ans[len(ans)-n]

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        points = []
        n = int(stdin.readline())
        sensor = list(map(int, stdin.readline().strip().split()))
        while sensor[0] != -1:
            points.append((sensor[0], sensor[1]))
            sensor = list(map(int, stdin.readline().strip().split()))
        print(solve(points,n))
main()