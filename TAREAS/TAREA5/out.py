"""
Nombre: Juan Esteban Becerra
Código: 8965694
"""
from sys import stdin

def solve(res):
    ans = None
    if len(perm) == 4:
        num = 0
        for n in count:
            if count[n] == 1:
                num = n
        if res - num == 0:
            ans = True
        else:
            ans = False
    else:
        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -=1
                if not ans:
                    ans = solve(res + n)
                if not ans:
                    ans = solve(res - n)
                if not ans:
                    if res % n == 0:
                        ans = solve(res // n)

                perm.pop()
                count[n] +=1
    #print(ans)
    return ans

def main():
    global nums, count, perm
    nums = list(map(int, stdin.readline().strip().split()))
    while sum(nums) != 0:
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] +=1
        ans = solve(23)
        if ans:
            print("Possible")
        else:
            print("Impossible")
        nums = list(map(int, stdin.readline().strip().split()))
main()