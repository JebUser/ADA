
def binsearch(A, low, hi, x):
    ans = None
    if low == hi:
        ans = False
    elif low+1 == hi:
        ans = A[low] == x 
    else:
        mid = low+((hi-low)>>1) #Para evitar solapamiento en cualquier lenguaje
        #mid = (low+hi)>>1 # Corrimiento de bits a la derecha !!EFICIENTE SIRVE
        #mid = (low+hi)//2
        if A[mid]==x:
            ans = True
        elif A[mid] < x:
            ans = binsearch(A, mid, hi, x)
        else:
            ans = binsearch(A, low, mid, x)

    return ans

def binsearchiterative(A, x):
    ans,low,hi = False,0,len(A)
    if low+1 != hi:
        while low+1!=hi:
            mid = low+((hi-low)>>1)
            if A[mid]<=x:
                low = mid
            else:
                hi = mid
        ans = A[low]==x


    return ans