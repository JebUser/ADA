"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 1134
"""
from sys import stdin

def solve(size, my_h, king_h):
    ans = 0
    l, r = 0,size-1,
    kl, kr = 0,size-1
    i = size
    while i != 0:
        if my_h[l] > king_h[kl]:
            ans+=200
            l+=1
            kl+=1
        elif my_h[r] > king_h[kr]:
            ans+=200
            r-=1
            kr-=1
        elif my_h[r] < king_h[kl]:
            ans-=200
            r-=1
            kl+=1
        i-=1
    return ans


def main():
    size = int(stdin.readline())
    while size != 0:
        my_h = list(map(int, stdin.readline().strip().split()))
        king_h = list(map(int, stdin.readline().strip().split()))
        my_h.sort(reverse=True)
        king_h.sort(reverse=True)
        print(solve(size, my_h, king_h))
        size = int(stdin.readline())

main()