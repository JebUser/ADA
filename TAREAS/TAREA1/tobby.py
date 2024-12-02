from sys import stdin
import heapq

def prior(k, priority):
    for i in range(k):
        element = heapq.heappop(priority)
        print(element[0], element[2])
        element[0]+=element[3]
        heapq.heappush(priority, element)
    
def main():
    c = int(stdin.readline())
    for i in range(c):
        priority = []
        n,k = map(int, stdin.readline().split())
        for j in range(n):
            name,t = map(str, stdin.readline().split())
            heapq.heappush(priority, [int(t), j, name, int(t)])
        prior(k, priority)
    return 0

main()
