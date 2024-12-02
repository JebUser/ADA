from sys import stdin

def max_cal(p, cal_res):
    ans = None
    if (p,cal_res) in mem:
        ans = mem[(p, cal_res)]
    else:
        if p == 0 and cal_res <= 0:
            ans = cal_res
        elif p == 0 and cal_res > 0:
            ans = -2501
        else:
            if cal_res <= 0:
                ans = cal_res
            else:
                ans = max(max_cal(p-1, cal_res), max_cal(p-1, cal_res - courses[p-1]))
        mem[(p, cal_res)] = ans
    return ans

def main():
    t = int(stdin.readline())
    for i in range(t):
        global cal_required, mem, courses
        cal_required = int(stdin.readline())
        p = int(stdin.readline())
        mem = {}
        courses = list(map(int, stdin.readline().strip().split()))
        res = max_cal(p, cal_required)
        if res != -2501 :
            print(cal_required - res)
        else:
            print("NO SOLUTION")

main()