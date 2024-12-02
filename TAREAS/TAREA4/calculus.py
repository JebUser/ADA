"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 1346
"""
#Asignar a los numeros mayores a las sumas
from sys import stdin

def process(expression):
    sumas,restas = 1,0
    lastSymb = '+'
    pila = []
    for i in expression:
        if i == '+':
            if len(pila) != 0:
                if pila[-1] == '-':
                    lastSymb = '-'
                    restas+=1
                else:
                    sumas+=1
                    lastSymb = '+' 
            else:
                sumas+=1
                lastSymb = '+'

        elif i == '-':
            if len(pila) != 0:
                if pila[-1] == '-':
                    lastSymb = '+'
                    sumas+=1
                else:
                    lastSymb = '-'
                    restas+=1  
            else:
                lastSymb = '-'
                restas+=1

        elif i == '(':
            pila.append(lastSymb)
        
        elif i == ')':
            pila.pop()
    
    return sumas, restas

def solve(sumas, restas, nums, numbers):
    ans = 0
    for i in range(numbers):
        if i < restas:
            ans-=nums[i]
        else:
            ans+=nums[i]
    
    print(ans)



def main():
    cases = int(stdin.readline())
    for i in range(cases):
        expression = stdin.readline()
        numbers = int(stdin.readline())
        nums = list(map(int, stdin.readline().strip().split()))
        nums.sort()
        sumas, restas = process(expression)
        solve(sumas, restas, nums, numbers)

main()