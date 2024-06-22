# from menu import *
from data.config.config import *

lista = read_data(r"code\data\config\palabras.json")
combianciones = list(lista[0].items())

import pygame
import random
import sys
from pygame.locals import *
from logica import *

palabra_secretita = random.choice(combianciones)
letras = palabra_secretita[0]
palabras_a_encontrar = palabra_secretita[1]
# print(palabras_a_encontrar)


ANCHO_VENTANA = 640
ALTO_VENTANA = 480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
TIEMPO_LIMITE = 30

def coincidencias(combinaciones, letras):

    set_dict = set(combinaciones)

    palabra = input("Ingrese la palabra: ").strip().lower()

    palabra_set = {palabra}

    intersec = set_dict.intersection(palabra_set)

    if len(intersec) > 0:
        retorno = palabra
    else:
        retorno = False

    return retorno

pygame.init()

fuente = pygame.font.SysFont("Arial", 40)

correctas = []
inicio_tiempo = pygame.time.get_ticks()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

jugando = True

while jugando:
    ventana.fill(BLANCO)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    tiempo_transcurrido = (pygame.time.get_ticks() - inicio_tiempo) // 1000
    tiempo_restante = TIEMPO_LIMITE - tiempo_transcurrido

    textito = fuente.render(f"TIEMPO RESTANTE: {tiempo_restante}", True, NEGRO)
    print(tiempo_restante)
    ventana.blit(textito, (200, 200))

    if tiempo_restante == 0:
        ventana.fill(VERDE)
        termina = fuente.render(f"FELICIDADES, ESPERASTE 30 SEGUNDOS!!!!", True, "red")
        ventana.blit(termina, (200, 200))
        pygame.display.update()
        pygame.time.delay(3000)
        jugando = False

    # if len(correctas) == 5:
    #     jugando = False
    # else:
    #     # ayuda = coincidencias(palabras_a_encontrar, letras)
    #     if ayuda == False:
    #         print("PALABRA INCORRECTA")
        
    #     elif ayuda:
    #         correcto = True
    #         for palabra in correctas:
    #             if palabra == ayuda:
    #                 print("          YA EXISTE           ")
    #                 correcto = False
    #                 break
            
    #         if correcto:
    #             correctas.append(ayuda)
    #             print("PALABRA CORRECTA")

    pygame.display.update()


pygame.quit()