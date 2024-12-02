from sys import stdin

def iterate(n,h,ta,td,heights):
    heights.sort()
    res,low,high = 0,0,n
    while low < high:
        if low != high-1:
            if heights[low] + heights[high-1] >= h:
                if heights[low] > heights[high-1]:
                    low+=1
                else:
                    high-=1
                res += ta
            else:
                if 2*ta > td: 
                    res += td
                else:
                    res += 2*ta
                low+=1
                high-=1
        else:
            res+=ta
            low+=1
    return res

def main():
    c = int(stdin.readline())
    for i in range(c):
        n,h,ta,td = map(int, stdin.readline().split())
        heights = list(map(int, stdin.readline().strip().split()))
        print(f"Case {i+1}: {iterate(n,h,ta,td,heights)}")
    return 0

main()