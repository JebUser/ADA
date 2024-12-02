"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 13082
"""
from sys import stdin

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        changes, seq = 0,1
        n = int(stdin.readline())
        sHeights = list(map(int, stdin.readline().strip().split()))
        for j in range(n):
            if sHeights[j] == seq:
                changes += 1
                seq+=1
        print(f"Case {i+1}:", n-changes)

main()
