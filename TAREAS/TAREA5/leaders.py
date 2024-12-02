"""
Nombre: Juan Esteban Becerra
Código: 8965694
"""
from sys import stdin

def solve(init, comb):
    if len(comb) == s:
        flag = True
        i = 0
        while i < len(banWords) and flag:
            if banWords[i][0] in comb and banWords[i][1] in comb:
                flag = False
            i+=1
        if flag:
            cadena = " ".join(comb)
            print(cadena)
    else:
        for j in range(init, t):
            comb.append(words[j])
            solve(j+1, comb)
            comb.pop()


def main():
    cases = int(stdin.readline())
    global t, s, words, banWords
    for i in range(cases):
        t, p, s = map(int, stdin.readline().strip().split())
        words = []
        for j in range(t):
            word = stdin.readline().rstrip()
            words.append(word.upper())
        banWords = []

        for k in range(p):
            w1, w2 = map(str, stdin.readline().split())
            banWords.append((w1.upper(), w2.upper()))
        words.sort()
        words.sort(key=len, reverse=True)
        print(f"Set {i+1}:")
        solve(0, [])
        print("")
main()