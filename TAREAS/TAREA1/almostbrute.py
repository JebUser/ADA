
def op1(lista, n1, n2):
    s1 = set()
    s2 = set()
    for i in lista:
        if n1 in i:
            s1 = set(i)
            i.clear()
        elif n2 in i:
            s2 = set(i)
            i.clear()
    lista.append(s1.union(s2))
    return lista

def op2(lista, n1, n2):
    for i in lista:
        if n1 in i:
            i.remove(n1)
        elif n2 in i:
            i.add(n1)
    return lista

def op3(lista, n):
    sum = 0
    size = 0
    for i in lista:
        if n in i:
            size = len(i)
            for j in i:
                sum+=j
    res = [size, sum]
    return res


def resolvedor(operaciones, lista):
    for operacion in operaciones:
        if operacion[0] == 1:
            op1(lista, operacion[1], operacion[2])
        elif operacion[0] == 2:
            op2(lista, operacion[1], operacion[2])
        else:
           print(' '.join(map(str, op3(lista, operacion[1]))))
    return 0

def main():
    n, m = map(int, input().split())
    operaciones = list()
    lista = list()
    for i in range(n):
        lista.append({i+1})
    for i in range(int(m)):
        operacion = list(map(int, input().split()))
        operaciones.append(operacion)

    print(operaciones)
        
    resolvedor(operaciones, lista)
    return 0
main()