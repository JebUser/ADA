from sys import stdin
def fibo_tab(n):
    tab = [None for _ in range(n+1)]
    tab[0], tab[1] = 0,1
    for i in range(0, n+1):
        tab[i] = tab[i-2] + tab[i-1]
    return tab[n]

def main():
    n = int(stdin.readline())
    print(fibo_tab(n))
main()