from functools import reduce
import pygame
import random
from data.config.config import *

diccionario = read_data(r"code\data\config\palabras.json")

def swap (lista:list, a:int, b:int):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def shuffle (letras:str) -> list[str]:
    letras = letras.split(", ")
    for i in range(len(letras)):
        new_index = random.randint(0,5)
        swap(letras, i, new_index)

    return letras
    # test = reduce(lambda last, actual)

def coincidencias(combinacion, diccionario):
    print(f"LA COMBINACION ES : {shuffle(combinacion)}")

    set_dict = set(diccionario[0][combinacion])

    palabra = input("Ingrese la palabra: ").strip().lower()

    palabra_set = {palabra}

    intersec = set_dict.intersection(palabra_set)

    if len(intersec) > 0:
        retorno = palabra
    else:
        retorno = False

    return retorno

palabra = coincidencias("P, R, O, A, E, S", diccionario)
print("Coincidencia:", palabra)

def sumar_puntaje (lista_coincidencias:list[str]) -> int:
    suma_puntaje = 0
    for coincidencia in lista_coincidencias:
        suma_puntaje += int(len(coincidencia))

    return suma_puntaje 

import time

contador = 90

while contador > 0:
    print(contador)
    time.sleep(1)
    contador -= 1

print("YAATA!!")