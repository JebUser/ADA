from sys import stdin

def sumdigits(n):
    result = 0
    #Recorre el numero como una lista y suma sus digitos
    for digit in str(n):
        result += int(digit)
    return result

def solver(result):
    res = None
    #Si el numero tiene 2 digitos se hace la op sumar digitos, en caso contrario se retorna
    if result < 10:
        res = result
    else:
        res = solver(sumdigits(result))
    return res

def main():
    num = int(stdin.readline())
    while (num != 0):
        print(solver(num))
        num = int(stdin.readline())
    return 0

main()