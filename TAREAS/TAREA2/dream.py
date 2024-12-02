from sys import stdin

def dream(ocur, list):
    median = (len(list))//2
    total_nums = ocur[list[median-1]]
    if (len(list)) % 2 == 1:
        print(list[median], total_nums, 1)
    else:
        total_nums += ocur[list[median]]
        print(list[median-1], total_nums, list[median] - list[median-1] + 1)

def main():
   nums = stdin.readline()
   while len(nums) != 0:
    list = []
    ocur = dict()
    for i in range(int(nums)):
        n = int(stdin.readline())
        if n in ocur:
            ocur[n] += 1
        else:
           ocur[n] = 1
        list.append(n)
    list.sort()
    dream(ocur, list)
    nums = stdin.readline()

main()