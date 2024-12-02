"""
Nombre: Juan Esteban Becerra Gutiérrez
Código: 8965694
"""
from sys import stdin

"""
Funcion solve
Globales:
    N: Tiempo de coccion de cada lado
    K: Numero de intervalos
    mem: memoria
    intervals: intervalos (li, lr)
Entradas:
    l1: tiempo de cocción del lado 1 de la carne
    l2: tiempo de cocción del lado 2 de la carne
    i: indexador para seleccionar cada intervalo
    side: booleano para saber si estoy en el lado 1 (True) o 2 (False)

Salida:
    Numero minimo de flips que se debe hacer en los intervalos


Funcionamiento
    La función solve recorre cada intervalo linealmente sumando 1 unidad de tiempo
    a un lado dependiendo que que lado este y haciendo un flip con la misma condicion.
    Evaulua el minimo entre seguir en el mismo lado, o sumar 1 a los flips y voltear al otro lado
    Termina cuando llega al final del intervalo, evaluando si ambos lados tienen el mismo tiempo de coccion
    retornado el numero de flips o infinito si ambos lados no son iguales o se pasan del tiempo de coccion N
"""

def solve(l1:int, l2:int, i:int, side:bool):
    ans = 0
    if (l1, l2, i, side) in mem:
        print("Ya hay", l1, l2, i, side)
        ans = mem[(l1, l2, i, side)]
    else: 
        #Mirar si la hamburguesa se cocina de más en un lado u otro
        if l1 > n or l2 > n:
            ans = float('inf')
        #Cuando la hamburguesa llega al tiempo 2N
        elif l1+l2 == 2*n:
            if l1 == l2:
                ans = 0
            else:
                ans = float('inf')
        else:
            #Si hay intervalos por recorrer
            if i != k-1:
                #Si todavia no llegamos al fin del intervalo
                if l1+l2 < intervals[i][1]:
                    if side:
                        ans = min(solve(l1+1, l2, i, side),
                                1 + solve(l1, l2+1, i, False))
                    else:
                        ans = min(1 + solve(l1+1, l2, i, True),
                                solve(l1, l2+1, i, side))

                #Llegamos al fin del intervalo       
                elif l1+l2 == intervals[i][1]:
                    jump = intervals[i+1][0] - intervals[i][1]
                    if side:
                        ans = min(solve(l1+jump, l2, i+1, side),
                                1 + solve(l1, l2+jump, i+1, False))
                    else:
                        ans = min(1 + solve(l1+jump, l2, i+1, True),
                                solve(l1, l2+jump, i+1, side))
            else:
                #Llegamos al ultimo intervalo
                if l1+l2 < intervals[i][1]:
                    if side:
                        ans = min(solve(l1+1, l2, i, side),
                                1 + solve(l1, l2+1, i, False))
                    else:
                        ans = min(1 + solve(l1+1, l2, i, True),
                                solve(l1, l2+1, i, side))
                
                #Llegamos al limite del ultimo intervalo
                elif l1+l2 == intervals[i][1]:
                    if side:
                        ans = min(solve(l1+ (2*n)-intervals[i][1], l2, i, side),
                                1 + solve(l1, l2+(2*n)-intervals[i][1], i, False))
                    else:
                        ans = min(1 + solve(l1+(2*n)-intervals[i][1], l2, i, True),
                                solve(l1, l2+(2*n)-intervals[i][1], i, side))
        print("Se guardo", l1, l2, i, side)
        mem[(l1, l2, i, side)] = ans
    return ans 
             

def main():
    cases = int(stdin.readline())
    global n, k, intervals, mem
    for i in range(cases):
        mem = {}
        ans = False
        n, k = map(int, stdin.readline().strip().split())
        intervals = []
        for j in range(k):
            li, lr = map(int, stdin.readline().strip().split())
            if li <= n and n <= lr:
                ans = True
            intervals.append((li, lr))

        if intervals[k-1][1] < n:
            print("Another bland and poorly cooked burger!")
        elif ans:
            print("Perfect burger!\n1")
        else:
            res = solve(intervals[0][0], 0, 0, True)
            if res != float('inf'):
                print("Perfect burger!")
                print(res)
            else:
                print("Another bland and poorly cooked burger!")


main()
