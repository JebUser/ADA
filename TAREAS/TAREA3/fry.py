from sys import stdin

def solve(t, f):
  ans = None
  if (t,f) in mem:
    ans = mem[(t,f)]
  else:
    if t == trips:
      ans = 0
    elif t != trips and f > trips:
      ans = (time_and_fuel[t][0]>>1) + solve(t+1, f+time_and_fuel[t][1])
    elif t != trips and f == 0:
      ans = time_and_fuel[t][0] + solve(t+1, f+time_and_fuel[t][1])
    else:
      ans = min(time_and_fuel[t][0] + solve(t+1, f+time_and_fuel[t][1]), (time_and_fuel[t][0]>>1) + solve(t+1, f+time_and_fuel[t][1]-1))
    mem[(t,f)] = ans
  return ans
     
def main():
  global trips, time_and_fuel, mem
  trips = int(stdin.readline())
  while trips != 0:
    time_and_fuel = []
    for i in range(trips):
      tn, en = map(int, stdin.readline().split())
      time_and_fuel.append((tn, en))
    mem = {}
    print(solve(0,0))
    trips = int(stdin.readline())

main()