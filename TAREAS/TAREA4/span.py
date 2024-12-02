"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 1346
"""

from sys import stdin

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
    mst = []
    connected = 0
    p, rango = [0 for _ in range(100)], [0 for _ in range(100)]

    for i in range(n):
        makeSet(i)
    i = 0
    while i != len(aristas) and connected != n-1:
        u,v = aristas[i][0],aristas[i][1]

        if findSet(u) != findSet(v):
            mst.append(aristas[i])
            unionSet(u,v)
            connected +=1
        i+=1

    return len(mst), mst

def span(aristas,n):
    sizeMst = n-1
    best = float('inf')
    mst = None
    aristas.sort(key = lambda x: x[2])
    i = 0
    while sizeMst == n-1:
        sizeMst, mst = kruskal(aristas[i:],n)
        span = mst[-1][2] - mst[0][2]
        if sizeMst == n-1:
            best = min(best, span)
        i+=1
    if best == float('inf'):
        print(-1)
    else:
        print(best)

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