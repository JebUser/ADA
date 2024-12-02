def subsetsum(A, n, x):
    ans = None
    if n==0:
        ans = x==0
    else:
        ans = subsetsum(A, n-1, x)
        if A[n-1] <= x:
            ans = ans or subsetsum(A, n-1, x-A[n-1])
    return ans