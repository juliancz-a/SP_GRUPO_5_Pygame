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
play_button = pygame.Rect(50,50,50,50) # rectangulo lógico
play_button_color = AZUL_CLARO
activo = False
text = "Jugar"
flag_run = True

gato = pygame.image.load(r"code\data\img\image.png")

gato_rect = gato.get_rect()

gato_rect.center = ((ANCHO_VENTANA/2, ALTO_VENTANA/2))

print(gato_rect)
# cajita = Box((150, 50), (150, 150))
# Box.set_text(cajita, "MARCELA")
# Box.set_color(cajita, "firebrick1")

while flag_run:
    #manejador central
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(evento.pos):
                print("JUGAR")
            # elif cajita.collidepoint(evento.pos):
            #     print("AYUDAAAAAAAAAA")


    ventana_principal.fill(BLANCO)

    text_surface = fuente.render(text, True, NEGRO)
    # ventana_principal.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    #rectangulo fisico
    pygame.draw.rect(ventana_principal, "firebrick1", play_button, border_radius=5 )
    # Box.render_box(cajita, ventana_principal)

    ventana_principal.blit(gato, gato_rect)
    pygame.display.update()

pygame.quit()