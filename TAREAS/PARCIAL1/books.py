from sys import stdin

def compare(mid, books, m):
    ans, i, ac = 1,0,0
    while i < len(books):
        if ac + books[i] <= mid:
            ac+= books[i]
        else:
            ans+=1
            ac = books[i]
        i+=1
    return ans

def solve(books, m):
    cad = ""
    ac = 0
    booksleft = len(books)
    scribeleft = m
    l,r = max(books),sum(books)
    while r != l:
        mid = l+((r-l)>>1)
        if compare(mid, books, m) <= m:
            r = mid
        else:
            l = mid+1

    i = len(books)-1
    noforcedist = True
    while i != -1:
        if noforcedist:
            if ac + books[i] <= l:
                cad = str(books[i]) + cad
                ac += books[i]
                booksleft -=1
            else:
                cad = str(books[i]) + " /" + cad
                ac = books[i]
                booksleft -=1
                scribeleft -=1
            
            if booksleft < scribeleft:
                noforcedist = False
        else:
            cad = str(books[i]) + " /" + cad
        if i != 0:
            cad = " " + cad
        #print(scribeleft, booksleft)
        i-=1
    return cad

def main():
    n = int(stdin.readline())
    for i in range(n):
        k, m = map(int, stdin.readline().strip().split())
        books = list(map(int, stdin.readline().strip().split()))
        print(solve(books, m))

main()