"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 11658
"""

from sys import stdin

def solve(coalit, n, curSum):
    ans = 0
    if (n, curSum) in mem:
        ans = mem[(n, curSum)]
    else:
        benefit = round((myStock*100/curSum),2)
        if n == 0:
            if curSum > 50 and coalit <= len(stocks)-1:
                ans = benefit
            else:
                ans = myStock
        else:
            if curSum > 50:
                ans = benefit
            else:
                ans = max(solve(coalit,n-1, curSum), solve(coalit+1, n-1, round((curSum + stocks[n-1]),2)))
        mem[(n, curSum)] = ans
    return ans

def main():
    n, x = map(int, stdin.readline().strip().split())
    while n != 0 and x != 0:
        global mem, stocks, myStock
        mem = dict()
        stocks = []
        for i in range(n):
            stock = float(stdin.readline())
            if i != x-1:
                stocks.append(stock)
            else:
                myStock = stock
        if myStock > 50:
            print("100.00")
        else:    
            print("{:0.2f}".format(solve(0, n-1, myStock)))
        n, x = map(int, stdin.readline().strip().split())

main()