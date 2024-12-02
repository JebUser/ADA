from sys import stdin

def sqrt(n):
    ans,low,hi = 1,1,n
    if low+1 != hi:
        while low+1 < hi:
            mid = low + (hi-low)//2
            if mid*mid <= n:
                low = mid
            else:
                hi = mid
        ans = low

    return ans*ans


def main():
    n = int(stdin.readline())
    while n != 0:
        print(sqrt(n))
        n = int(stdin.readline())

main()
