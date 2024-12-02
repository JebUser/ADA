"""
Nombre: Juan Esteban Becerra Gutiérrez
Código
"""
from sys import stdin

def solve(l1:int, l2:int, i:int, time:int, side:bool):
    ans = 0
    if (l1, l2, i, time, side) in mem:
        ans = mem[(l1, l2, i, time, side)]
    else: 
        #Mirar si la hamburguesa se cocina de más en un lado u otro
        #Cuando la hamburguesa llega al tiempo 2N
        if time == 2*n:
            if l1 == l2:
                ans = 0
            elif l1 != l2:
                ans = float('inf')
            else:
                ans = float('inf')
        else:
            #Si hay intervalos por recorrer
            if i != k-1:
                #Si todavia no llegamos al fin del intervalo
                if time < intervals[i][1]:
                    rest = intervals[i][1]-intervals[i][0]
                    #Lado 1
                    if side:  
                        if time == intervals[i][0]:
                            ans = min(
                                solve(l1+rest, l2, i, intervals[i][1], side), #Todo LADO 1
                                1 + solve(l1, l2+rest, i, intervals[i][1], False), #Todo lado 2
                                solve(l1, l2, i, time+1, side)) #Casos de combinaciones
                        else:
                            #print('aca1')
                            for j in range(intervals[i][0], intervals[i][1]+1):
                                ans = min(
                                    1 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], False),
                                    2 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], side)
                                )
                    #Lado 2
                    else:
                        if time == intervals[i][0]:
                            ans = min(
                                1 + solve(l1+rest, l2, i, intervals[i][1], True), #Todo LADO 1
                                solve(l1, l2+rest, i, intervals[i][1], side), #Todo lado 2
                                solve(l1, l2, i, time+1, side)) #Casos de combinaciones
                        else:
                            #print('aca2')
                            for j in range(intervals[i][0], intervals[i][1]+1):
                                #print(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j))
                                ans = min(
                                    1 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], True),
                                    2 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], side)
                                )

                #Llegamos al fin del intervalo       
                elif time == intervals[i][1]:
                    #print(l1, l2)
                    #if intervals[i][0] == intervals[i][1]:
                        #print("Ultimo", intervals[i])
                    jump = intervals[i+1][0] - intervals[i][1]
                    if side:
                        ans = min(
                            solve(l1+jump, l2, i+1, time+jump, side),
                            1 + solve(l1, l2+jump, i+1, time+jump, False))
                    else:
                        ans = min(
                            1 + solve(l1+jump, l2, i+1, time+jump, True),
                            solve(l1, l2+jump, i+1, time+jump, side))
            else:
                #Llegamos al ultimo intervalo
                if time < intervals[i][1]:
                    rest = intervals[i][1]-intervals[i][0]
                    #Lado 1
                    if side:
                        if time == intervals[i][0]:
                            ans = min(
                                solve(l1+rest, l2, i, intervals[i][1], side), #Todo LADO 1
                                1 + solve(l1, l2+rest, i, intervals[i][1], False), #Todo lado 2
                                solve(l1, l2, i, time+1, side))
                        else:
                            #print('aca3')
                            for j in range(intervals[i][0], intervals[i][1]+1):
                                ans = min(
                                    1 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], False),
                                    2 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], side)
                                )
                    #Lado 2
                    else:
                        if time == intervals[i][0]:
                            ans = min(
                                1 + solve(l1+rest, l2, i, intervals[i][0], True), #Todo LADO 1
                                solve(l1, l2+rest, i, intervals[i][0], side), #Todo LADO 2
                                solve(l1, l2, i, time+1, side)) #Combinaciones 
                        else:
                            #print('aca4')
                            for j in range(intervals[i][0], intervals[i][1]+1):
                                #print(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j))
                                ans = min(
                                    1 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], True),
                                    2 + solve(l1+(j-intervals[i][0]), l2+(intervals[i][1] - j), i, intervals[i][1], side)
                                )

                
                #Llegamos al limite del ultimo intervalo
                if time == intervals[i][1]:
                    if side:
                        ans = min(
                            solve(l1+ (2*n)-intervals[i][1], l2, i, 2*n, side),
                            1 + solve(l1, l2+(2*n)-intervals[i][1], i, 2*n, False))
                    else:
                        ans = min(
                            1 + solve(l1+(2*n)-intervals[i][1], l2, i, 2*n, True),
                            solve(l1, l2+(2*n)-intervals[i][1], i, 2*n, side))
                        
        mem[(l1, l2, i, time, side)] = ans
    print(ans)
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
            res = solve(intervals[0][0], 0, 0, intervals[0][0], True)
            if res != float('inf'):
                print("Perfect burger!")
                print(res)
            else:
                print("Another bland and poorly cooked burger!")

main()