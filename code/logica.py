letras = ['L', 'A', 'C', 'E', 'T', 'O']

from functools import reduce
import random

def swap (lista:list, a:int, b:int):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def shuffle (letras:list[str]) -> list[str]:
    for i in range(len(letras)):
        new_index = random.randint(0,5)
        swap(letras, i, new_index)

    return letras
    # test = reduce(lambda last, actual)
print(shuffle(letras))