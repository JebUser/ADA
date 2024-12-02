"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 1346
"""

from sys import stdin

def divide(amounts, p, n):
    lans = [0] * n
    aLeft = p
    for i in range(n):
        div = aLeft//(n-i)
        if amounts[i][0] < div:
            lans[amounts[i][1]] = amounts[i][0]
            aLeft-= amounts[i][0]
        else:
            lans[amounts[i][1]] = div
            aLeft-= div
    return lans

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        amounts = []
        p,n = map(int, stdin.readline().strip().split())
        nums = list(map(int, stdin.readline().strip().split()))
        for i in range(n):
            amounts.append((nums[i], i))
        amounts.sort(key = lambda x: (x[0], -x[1]))
        if sum(nums) < p:
            print('IMPOSSIBLE')
        else:
            ans = divide(amounts, p, n)
            cad = str(ans[0])
            for i in range(1, n):
                cad = cad + " " + str(ans[i])
            print(cad)

main()