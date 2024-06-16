import pygame
#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
DIMENSIONES = (ANCHO_VENTANA, ALTO_VENTANA)

ventana_principal = pygame.display.set_mode((DIMENSIONES))
pygame.display.set_caption("JUEGO")

ventana_principal.fill(BLANCO)

fuente = pygame.font.SysFont("Arial", 20)

#Cuadro de texto (Orientarlo a objetos reciba dimensiones, colores, donde lo quiero ubicar, preguntarle si quiere tener un texto por default)
play_button = pygame.Rect(50,50,200,32) # rectangulo lógico
play_button_color = AZUL_CLARO
activo = False
text = "Jugar"
flag_run = True

while flag_run:
    #manejador central
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(evento.pos):
                print("JUGAR")


    ventana_principal.fill(BLANCO)

    text_surface = fuente.render(text, True, NEGRO)
    # ventana_principal.blit(text_surface, (input_box.x + 5, input_box.y + 5))


    #rectangulo fisico
    pygame.draw.rect(ventana_principal, play_button_color, play_button)

    pygame.display.update()

pygame.quit()