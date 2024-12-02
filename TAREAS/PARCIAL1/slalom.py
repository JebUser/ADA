from sys import stdin

def check(mid, gates, w, vh):
  ans = True
  v = mid
  ni = gates[0][0] #puerta actual a i
  nd = gates[0][0] + w #puerta actual a la d
  i = 1
  while i < len(gates) and ans == True:
    t = (gates[i][1] - gates[i-1][1]) / v

    nexti = gates[i][0] 
    nextd = gates[i][0] + w
    newi = ni - t * vh #donde voy izquierda
    newd = nd + t * vh #donde voy derecha

    ni = max(newi, nexti)
    nd = min(newd, nextd)
    if ni > nd:
      ans = False
    i+=1
    #print(newi, newd)

  return ans

def min_sp(gates,skis, w, vh):
  l, r = 0, len(skis)-1
  while l <= r:
    mid = l + ((r-l)>>1)
    if check(skis[mid], gates, w, vh):
      l = mid + 1
    else:
      r = mid - 1

  if r < 0:
    print("IMPOSSIBLE")
  else:
    print(skis[r])

def main():
    c = int(stdin.readline())
    for i in range(c):
        w, vh, n = map(int, stdin.readline().strip().split())
        gates = []
        for k in range(n):
            x, y =  map(int, stdin.readline().strip().split())
            gates.append((x,y))
        s = int(stdin.readline())
        skis = []
        for j in range(s):
            skis.append(int(stdin.readline()))
        
        skis.sort()
        min_sp(gates,skis, w, vh)

main()