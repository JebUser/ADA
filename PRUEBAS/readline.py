from sys import stdin


def main():
    n,m = map(int, stdin.readline().split())
    print(n)
    for i in range(int(m)):
        operations = list(map(int, stdin.readline().strip().split()))
        print(operations)
    return 0

main()
