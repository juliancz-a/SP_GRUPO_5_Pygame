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
        "repo", "rapo", "pos", "rap", "res", "par"
    ],

    "R, C, A, E, S, E": 
    [
        "aceras", "acreas", "arcase", "arceas",
        "careas", "caresa", "casare", "casera",
        "resaca", "sacare", "sacare", "secara",
        "cesara", "cesara", "escara"
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

