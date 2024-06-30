import pygame
import random
from game_tools.class_box import Box  
from constantes import *

def draw_words (surface, matrix, words_founded:list, comodin, random_letter):
    
    x = 55
    
    for i in range (len(matrix)):
        printed = 0
        y = 530
        x += 100
        for j in range (len(matrix[i])):

            if printed == 6 and j != len(matrix[i]) - 1:
                y = 530
                x += 100
                printed = 0

            elif j == len(matrix[i]) - 1 and printed == 6:
                printed = 0

            if matrix[i][j] != 0:
                word = matrix[i][j]
                word_text = word
                word = Box((x, y), (40, 100))

                if comodin == 0:
                    letter = use_comodin(random_letter, words_founded, word_text)
                    if letter[0] != False:
                        letter_box = Box((x + letter[1],y), (40,100))

                        letter_box.draw_text(surface, letter[0], COLOR_PALABRA, FUENTE_3, font_size=200, outline="shadow")

                for word_founded in words_founded:
                    if word_founded == matrix[i][j]:
                        word.draw_text(surface,word_text, COLOR_PALABRA, FUENTE_3, font_size=200, outline="shadow")
                        break
        
                word.draw_text(surface,f"_"*(6-i), COLOR_PALABRA, FUENTE_3, font_size=250)
                
                y += 20
                printed +=1

def sum_score(scoreboard:int, word):
    scoreboard += len(word)
    return scoreboard

def normalize_words (combinations):
    palabras = {3: [], 4: [], 5: [], 6: []}

    for combination in combinations:
        for key in palabras.keys():
            if len(combination) == key:
                palabras[key].append(combination)

    max_len = ordenar_elementos([len(palabras[3]), len(palabras[4]), len(palabras[5]), len(palabras[6])], 1)

    matriz = [[0] * max_len for _ in range(4)]

    for i in range (len(matriz)):
        for j in range (len(palabras[6-i])):
                matriz[i][j] = palabras[6-i][j]
    print(matriz)

    return matriz


def select_random_letter (combinaciones):
    elemento_random = random.randint(0, len(combinaciones) - 1)
    palabra = combinaciones[elemento_random]
    
    letra = palabra[random.randint(0, len(palabra) - 1)]

    return letra

def use_comodin (letter, words_founded, word_text):
    pos = 0
  
    for matrix_letter in word_text:
        if matrix_letter == letter:
            coincidence = True
            break
        pos += 12

    for word_founded in words_founded:
        if word_founded == word_text:
            coincidence = False

    if coincidence == False:
        letter, pos = False, False
    return letter,pos

def count_select_letters (selected_letters:list) -> int:
    count = 0
    for letter in selected_letters:
        if letter != "":
            count += 1
    
    return count

def set_combination (lista:list[dict]) -> tuple:
    #key, values
    lista_letras = list(lista[0].keys())
    letras = random.choice(lista_letras)

    combinaciones = lista[0].pop(letras)

    datos = letras, combinaciones

    return datos
    
def ordenar_elementos (list:list[dict], orden:int):

    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            match orden:
                case 1:
                    if list[i] >= list[j]:
                            swap(list, i, j)
                case 2:
                    if list[i] <= list[j]:
                        swap(list, i, j)
    return list.pop()

def swap(list:list[dict], a:int, b:int):
    aux = list[a]
    list[a] = list[b]
    list[b] = aux
