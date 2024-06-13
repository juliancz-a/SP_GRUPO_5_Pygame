letras = ['L', 'A', 'C', 'E', 'T', 'O']

from functools import reduce
import pygame
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


diccionario = [
    {"P, R, O, A, E, S": 
    [
        "aperos", "apreso", "aproes", "arpeos",
        "aspero", "espora", "operas", "opresa",
        "pareos", "pasero", "peoras", "posare", 
        "raspeo", "repaso", "reposa", "separo",
        "sopare", "sopear", "sopera", "pares",
        "opera", "preso", "sopar", "rapos", "paseo",
        "pera", "pose", "paro", "ropa", "sapo", 
        "repo", "rapo", "pos", "rap", "res", "par", "por"
    ],

    "A, S, R, C, E, A": 
    [
        "aceras", "acreas", "arcase", "arceas",
        "careas", "caresa", "casare", "casera",
        "resaca", "sacare", "secara", "resaca",
        "cesara", "escara", "seca", "caer", "rasca",
        "res", "casar", "arcas", "asear", "secar",
        "ser", "era", "cera", "crea", "esa", "sea",
        "cara", "ras", "arca"
    ],
    "A, R, P, O, T, E": 
    [
        "aporte", "apreto", "atrope", "optare", "patero", 
        "poetar", "portea", "potare", "potear", "potera", 
        "potrea", "ropeta", "topare", "topear", "topera", 
        "trapeo", "trapo", ""
    ]
    }
    ]


def coincidencias(combinacion: dict[str]):
    set_dict = set(diccionario[0][combinacion])

    palabra = input("Ingrese la palabra: ").strip().lower()

    palabra_set = {palabra}

    intersec = set_dict.intersection(palabra_set)

    if len(intersec) > 0:
        retorno = palabra
    else:
        retorno = False

    return retorno

palabra = coincidencias("R, C, A, E, S, E")
print("Coincidencia:", palabra)

