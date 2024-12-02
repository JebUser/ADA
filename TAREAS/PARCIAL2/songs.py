"""
Nombre: Juan Esteban Becerra
Código: 8965694
UVA: 1346
"""
from sys import stdin

def main():
    songs = stdin.readline()
    while songs != "":
        playlist = []
        i = int(songs)
        while i != 0:
            line = stdin.readline().strip().split()
            i -= len(line)/3
            for j in range(0, len(line), 3):
                playlist.append([int(line[j]), float(int(line[j+1])/float(line[j+2]))])
        index = int(stdin.readline())
        playlist.sort(key = lambda x: x[1])
        print(playlist[index-1][0])
        songs = stdin.readline().rstrip("\n")
main()