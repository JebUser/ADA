from sys import stdin

def solve(n,k):
  ans = None

  return ans

def main():
  global mem, w_apples
  cases = int(stdin.readline())
  for i in range(cases):
    mem = {}
    w_apples = []
    n, k = map(int, stdin.readline().split())
    for j in range(1+k, n+1):
      w_apples.append(j)
    print(f"Case {i+1}: {w_apples}")

main()