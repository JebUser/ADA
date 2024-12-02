from sys import stdin

def stern(n,m):
    ans = ""
    left = [0,1]
    right = [1,0]
    mid = [1,1]
    while mid[0] != n or mid[1] != m:
        v1 = n*mid[1]
        v2 = m*mid[0]
        if v1 < v2:
            right = mid
            mid = [left[0]+mid[0], left[1]+mid[1]]
            ans += "L"
        else:
            left = mid
            mid = [mid[0]+right[0], mid[1]+right[1]]
            ans += "R"
    return ans

def main():
    n, m = map(int, stdin.readline().strip().split())
    while n != 1 or m != 1:
        print(stern(n,m))
        n, m = map(int, stdin.readline().strip().split())

main()