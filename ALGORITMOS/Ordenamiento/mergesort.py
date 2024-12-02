"""
Merge Sort
"""

from sys import stdin

MAX = 100000
AUX = [None for _ in range(MAX)]

def mergesort(A, low, hi):
  if low + 1 < hi:
    mid = low + ((hi - low) >> 1)    # mid = (low+hi)//2
    mergesort(A, low, mid)
    mergesort(A, mid, hi)
    merge(A, low, mid, hi)

def merge(A, low, mid, hi):
  for i in range(low, hi):
    AUX[i] = A[i]

  i, left, right = low, low, mid
  while i != hi:
    if left == mid:
      A[i] = AUX[right]
      right +=1
    elif right == hi:
      A[i] = AUX[left]
      left += 1
    else:
      if AUX[left] <= AUX[right]:
        A[i] = AUX[left]
        left += 1
      else:
        A[i] = AUX[right]
        right +=1
    print(A[i])
    i += 1
    
l = [54, 23, 56, 88, 24, 24, 12, 5, 20, 33, 33, 33, 33]
mergesort(l, 0, len(l))
print(l)