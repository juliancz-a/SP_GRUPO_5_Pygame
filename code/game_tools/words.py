import pygame
import random
from game_tools.class_box import Box  
from game_tools.extra_functions import *
from constantes import *

def draw_words (surface: pygame.Surface, matrix: list, words_founded: list, comodin_state: int, random_letter: str) -> None:
    """
    Recorre la matriz con las palabras que se encuentran en el diccionario de la
    combinación de letras encontrada, y las muestra en pantalla, sin ser reveladas.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        matrix (list): Matriz con todas las palabras que se encuentran dentro de la combinación
        de letras elegida.
        words_founded (list): Lista de palabras que ya fueron encontradas.
        comodin_state (int): Recibe el estado de uso del comodin.
        random_letter (str): Recibe la letra aleatoria que el comodin deberá mostrar.
    """
    x = 55
    
    for i in range (len(matrix)):
        printed = 0
        y = 530
        x += 100
        for j in range (len(matrix[i])):
    
            if matrix[i][j] != 0:
                word = matrix[i][j]
                word_text = word
                word = Box((x, y), (40, 100))

                if comodin_state == 0:
                    use_comodin(surface, random_letter, words_founded, word_text, x, y)

                for word_founded in words_founded:
                    if word_founded == matrix[i][j]:
                        word.draw_text(surface, word_text, COLOR_PALABRA, FUENTE_3, font_size=200, outline="shadow")
                        break
        
                word.draw_text(surface, f"_"*(6-i), COLOR_PALABRA, FUENTE_3, font_size=250)
                
                y += 20
                printed +=1
            
                if printed == 6 and j != len(matrix[i]) - 1:
                    y = 530
                    x += 100
                    printed = 0
            else:
                if printed == 0:
                    x -= 100
                break

def sum_score(score:int, word):
    score += len(word)
    return score

def normalize_words (combinations: list) -> list[list]:
    """
    Recibe una lista de palabras, y las transforma en una matriz,
    la cual se divide según la longitud de las mismas.

    Args:
        combinations (list): La lista con todas las palabras a encontrar.

    Returns:
        list[list]: La matriz con las palabras ordenadas según la longitud.
    """
    palabras = {3: [], 4: [], 5: [], 6: []}

    for combination in combinations:
        for key in palabras.keys():
            if len(combination) == key:
                palabras[key].append(combination)

    max_len = ordenar_elementos([len(palabras[3]), len(palabras[4]), len(palabras[5]), len(palabras[6])], 2)
    
    matriz = [[0] * max_len for _ in range(4)]

    for i in range (len(matriz)):
        for j in range (len(palabras[6-i])):
                matriz[i][j] = palabras[6-i][j]

    return matriz

def select_random_letter(combinaciones: list) -> str:
    """
    Extrae una letra aleatoria de una lista de palabras.

    Args:
        combinaciones (list): Lista con todas las palabras a encontrar.

    Returns:
        str: Letra para el comodin
    """
    elemento_random = random.randint(0, len(combinaciones) - 1)
    palabra = combinaciones[elemento_random]
    
    letra = palabra[random.randint(0, len(palabra) - 1)]

    return letra

def use_comodin(surface: pygame.Surface, letter: str, words_founded: list, word_text: str, x: int, y: int) -> None:
    """
    Muestra la letra que el comodin deberá mostrar en la pantalla, en cada una de las palabras
    que todavía no fueron encontradas.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        letter (str): Letra aleatoria.
        words_founded (list): Lista con todas las palabras ya encontradas.
        word_text (str): Palabra a analizar, para el uso del comodin.
        x (int): Coordenada horizontal en la superficie.
        y (int): Coordenada vertical en la superficie.
    """
    pos = 0
    coincidence = False
    
    for matrix_letter in word_text:
        if matrix_letter == letter:
            coincidence = True
            break
        pos += 12

    for word_founded in words_founded:
        if word_founded == word_text:
            coincidence = False

    if coincidence:
        letter_box = Box((x + pos ,y), (40,100))

        letter_box.draw_text(surface, letter[0], COLOR_PALABRA, FUENTE_3, font_size=200, outline="shadow")

def count_select_letters (selected_letters: list) -> int:
    """
    Cuenta la cantidad de letras seleccionadas.

    Args:
        selected_letters (list): Letras seleccionadas.

    Returns:
        int: Cantidad de letras seleccionadas.
    """
    count = 0
    for letter in selected_letters:
        if letter != "":
            count += 1
    
    return count

def set_combination (lista: list[dict]) -> tuple:
    """
    Desde una lista con diccionarios, elige uno aleatorio, para extraer
    su key y su value.

    Args:
        lista (list[dict]): Lista con diccionarios.

    Returns:
        tuple: Tupla con la key, y su value.
    """
    lista_letras = list(lista[0].keys())
    letras = random.choice(lista_letras)

    combinaciones = lista[0].pop(letras)

    datos = letras, combinaciones

    return datos