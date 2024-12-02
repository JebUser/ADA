def merge_sort_iterativo(lista):
    tamaño = 1
    n = len(lista)
    
    while tamaño < n:
        izquierda = 0
        while izquierda < n - tamaño:
            medio = izquierda + tamaño - 1
            derecha = min((izquierda + 2 * tamaño - 1, n - 1))
            merge(lista, izquierda, medio, derecha)
            izquierda += 2 * tamaño

        tamaño *= 2

def merge(lista, izquierda, medio, derecha):
    i = izquierda
    j = medio + 1
    temp = []

    while i <= medio and j <= derecha:
        if lista[i] < lista[j]:
            temp.append(lista[i])
            i += 1
        else:
            temp.append(lista[j])
            j += 1

    while i <= medio:
        temp.append(lista[i])
        i += 1

    while j <= derecha:
        temp.append(lista[j])
        j += 1

    for k in range(len(temp)):
        lista[izquierda + k] = temp[k]

# Ejemplo de uso
mi_lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort_iterativo(mi_lista)
print("Lista ordenada:", mi_lista)
