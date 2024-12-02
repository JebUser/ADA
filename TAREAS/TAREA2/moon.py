from sys import stdin

def bisection(t, d):
    ans,low,hi = 0, -1, t+1
    while low+1 < abs(hi):
        mid = low + ((abs(hi)-low)>>1)
        if mid*t <= abs(d):
            low = mid
        else:
            hi = mid
    ans = low

    return ans

def moons(t,d):
    t *= 86400
    d *= 1000000
    v = bisection(t,d)
    if d/t > 1:
        print(f"Remove {int(v)} tons")
    elif d/t < 0:
        print(f"Add {int(v)} tons")
    else:
        print("Add 0 tons")


def main():
    n = int(stdin.readline())
    for i in range(n):
        t,s,d = map(int, stdin.readline().strip().split())
        moons(t,d)

main()