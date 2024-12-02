from sys import stdin
def fib_memo(n, memo):
    ans = None
    if n in memo:
        ans = memo[n]
    else:
        if n <= 1: ans = n
        else:
            ans = fib_memo(n-2, memo) + fib_memo(n-1, memo)
            memo[n] = ans
    return ans

def main():
    memo = dict()
    n = int(stdin.readline())
    print(fib_memo(n, memo))
    print(memo)
main()
