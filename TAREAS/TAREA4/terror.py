"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 12834
"""

from sys import stdin

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        profit= 0
        n,k = map(int, stdin.readline().strip().split())
        needed = list(map(int, stdin.readline().strip().split()))
        generated = list(map(int, stdin.readline().strip().split()))
        recollected = []

        for l in range(n):
            recollected.append(generated[l]-needed[l])
        recollected.sort(reverse=True)

        j = n-1
        for m in range(k):
            if recollected[j] < 0:
                n-=1
            j-=1
        
        for t in range(n):
            profit+=recollected[t]
        if profit <= 0:
            print(f"Case {i+1}: No Profit")
        else:
            print(f"Case {i+1}:", profit)

main()