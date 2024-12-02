from sys import stdin
fib = [0, 1]
for j in range(2, 45):
    fib.append(fib[j-1] + fib[j-2])
fib.remove(0)
fib.remove(1)

def power(n):
    ans = 1
    for i in range(n):
        ans *= 2
    return ans
# Retorno el numero fibonacci y la posicion donde esta
def bisection(n):
    ans,low,hi = 0,0,len(fib)
    if low+1 != hi:
        while low+1 != hi:
            mid = low + (hi-low)//2
            if n < fib[mid]:
                hi = mid
            else:
                low = mid
        ans = low

    return ans, fib[low]

def pinary(n):
    ans = 0
    num = bisection(n) #Encuentro su fibonacci mas cercano a la izq
    index = n - num[1] # Para hallar el index del nuevo fibonacci a encontrar
    while index > 0:
        ans += power(num[0])
        num = bisection(index)
        index -= num[1] #Al numero le resto El fibonacci más cercano del index pasado

    ans += power(num[0])
    return bin(ans)[2:]


def main():
    cases = int(stdin.readline())
    for i in range(cases):
        n = int(stdin.readline())
        print(pinary(n))
    return 0

main()