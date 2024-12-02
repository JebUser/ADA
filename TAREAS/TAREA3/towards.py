from sys import stdin

def check(row, colum):
  ans = None
  if row >= n: 
    ans = [colum, colum+1]
  else:
    ans = []
    if colum != 0: 
      ans.append(colum-1)
    if colum != row: 
      ans.append(colum)
  return ans

def calculate(row, colum, num):
  ans = None
  if (row,colum,num) in mem: 
    ans = mem[(row,colum,num)]
  else:
    if row == 0: 
      ans = abs(board[0][0]) == abs(num)
    else:
      ans = False
      n = 0
      next = check(row,colum)
      while ans == False and n != len(next):
        ans = calculate(row-1, next[n], num+board[row][colum]) or calculate(row-1, next[n], num-board[row][colum])
        n += 1
    mem[(row,colum,num)] = ans
  return ans

def solve():
  ans = None
  n = 0
  res = False
  while res == False:
    res = calculate(rows-1, 0, n) or calculate(rows-1, 0, -n)
    if res: 
      ans = n
    n += 1
  return ans

def main():
  global board, n, rows, mem
  n = int(stdin.readline())
  while n!=0:
    mem = {}
    rows = 2*n-1
    board = [ list(map(abs, map(int, stdin.readline().split()))) for _ in range(rows) ]
    print(solve())
    n = int(stdin.readline())

main()