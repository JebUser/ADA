from sys import stdin

def find_root(parents, x):
    ans = None
    if parents[x] == x: 
        ans = x
    else:
        parents[x] = find_root(parents, parents[x])
        ans = parents[x]
    return ans

def union(parents, ranks, sums, digits, x, y):
    root_x = find_root(parents, x)
    root_y = find_root(parents, y)


    if root_x != root_y:
        if ranks[root_x] < ranks[root_y]: 
            root_x, root_y = root_y, root_x
        
        sums[root_x] += sums[root_y]
        digits[root_x] += digits[root_y]

        parents[root_y] = root_x

        if ranks[root_x] == ranks[root_y]: 
            ranks[root_x] += 1

def remove(parents, ranks, sums, digits, x, y):

    root_x = find_root(parents, x)
    root_y = find_root(parents, y)

    if root_x != root_y:
        sums[root_x] -= x
        digits[root_x] -= 1
        ranks[root_x] = 0

        sums[root_y] += x
        digits[root_y] +=1

        if ranks[root_y] == 0:
            ranks[root_y]+=1

        parents[x] = root_y


def main():
    line = stdin.readline()
    while len(line) != 0:
        n,m = map(int, line.split())

        ranks = [0] * (2*n+1) 
        parents = [0] * (2*n+1)
        digits = [0] * (2*n+1)
        sums = [0] * (2*n+1)
        for i in range(1, n + 1):
            j = n + i
            parents[i] = j
            parents[j] = j
            digits[j] = 1
            sums[j] = i

        operations = list()

        for i in range(int(m)):
            operations = list(map(int, stdin.readline().strip().split()))
            if operations[0] == 1:
                union(parents, ranks, sums, digits, operations[1], operations[2])
            elif operations[0] == 2:
                remove(parents, ranks, sums, digits, operations[1], operations[2])
            elif operations[0] == 3:
                num = find_root(parents, operations[1])
                print(digits[num], sums[num])

        line = stdin.readline()

main()