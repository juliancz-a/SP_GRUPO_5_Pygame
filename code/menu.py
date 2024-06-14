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
input_box = pygame.Rect(50,50,200,32) # rectangulo lógico
color_inactivo = AZUL
color_activo = ROJO
color_actual = color_inactivo
activo = False
text = ""
flag_run = True

while flag_run:
    #manejador central
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(evento.pos):
                activo = not activo

            if activo:
                color_actual = color_activo
            else:
                color_actual = color_inactivo

        elif evento.type == pygame.KEYDOWN:
            if activo:
                if evento.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    text = ""
                else: 
                    text += evento.unicode



    ventana_principal.fill(BLANCO)

    text_surface = fuente.render(text, True, NEGRO)
    ventana_principal.blit(text_surface, (input_box.x + 5, input_box.y + 5))


    #rectangulo fisico
    pygame.draw.rect(ventana_principal, color_actual, input_box, 2)

    pygame.display.update()

pygame.quit()