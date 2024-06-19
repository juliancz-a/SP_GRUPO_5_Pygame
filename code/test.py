# import pygame
# import sys

# # Inicializar Pygame
# pygame.init()

# # Configuración de la pantalla
# ANCHO_INICIAL = 800
# ALTO_INICIAL = 600
# ventana = pygame.display.set_mode((ANCHO_INICIAL, ALTO_INICIAL), pygame.RESIZABLE)
# pygame.display.set_caption('Juego Redimensionable')

# # Colores
# BLANCO = (255, 255, 255)
# ROJO = (255, 0, 0)
# AZUL = (0, 0, 255)

# # Fuente para el texto
# fuente = pygame.font.SysFont(None, 36)

# # Posiciones originales y dimensiones de los elementos
# elementos = {
#     "boton_jugar": {
#         "rect": pygame.Rect(100, 100, 200, 50),
#         "color": AZUL,
#         "text": "Jugar",
#     },
#     "caja_texto": {
#         "rect": pygame.Rect(400, 300, 300, 100),
#         "color": ROJO,
#         "text": "Texto",
#     }
# }

# # Guardar las posiciones y dimensiones originales
# elementos_originales = {
#     key: elem["rect"].copy() for key, elem in elementos.items()
# }

# # Función para redimensionar elementos proporcionalmente
# def redimensionar_elementos(nueva_ventana, elementos, elementos_originales):
#     ancho_ventana, alto_ventana = nueva_ventana.get_size()
    
#     for key, elem in elementos.items():
#         rect_original = elementos_originales[key]
#         rect = elem["rect"]
        
#         # Escalar la posición y dimensiones de los elementos proporcionalmente
#         rect.x = int(rect_original.x * ancho_ventana / ANCHO_INICIAL)
#         rect.y = int(rect_original.y * alto_ventana / ALTO_INICIAL)
#         rect.width = int(rect_original.width * ancho_ventana / ANCHO_INICIAL)
#         rect.height = int(rect_original.height * alto_ventana / ALTO_INICIAL)

# # Función para restaurar las posiciones y dimensiones originales
# def restaurar_elementos(elementos, elementos_originales):
#     for key in elementos:
#         elementos[key]["rect"] = elementos_originales[key].copy()

# # Bucle principal del juego
# def main():
#     flag_run = True

#     while flag_run:
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 flag_run = False
#             elif evento.type == pygame.VIDEORESIZE:
#                 nueva_ventana = pygame.display.set_mode(evento.size, pygame.RESIZABLE)
#                 redimensionar_elementos(nueva_ventana, elementos, elementos_originales)
#                 # Restaurar si el tamaño es el original
#                 if evento.size == (ANCHO_INICIAL, ALTO_INICIAL):
#                     restaurar_elementos(elementos, elementos_originales)

#         ventana.fill(BLANCO)

#         # Dibujar elementos
#         for key, elem in elementos.items():
#             pygame.draw.rect(ventana, elem["color"], elem["rect"])
#             text_surface = fuente.render(elem["text"], True, BLANCO)
#             text_rect = text_surface.get_rect(center=elem["rect"].center)
#             ventana.blit(text_surface, text_rect)

#         pygame.display.update()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()


import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 200),HWSURFACE|DOUBLEBUF|RESIZABLE)
    fake_screen = screen.copy()
    pic = pygame.surface.Surface((50, 50))
    pic.fill((255, 100, 200))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.display.quit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

        fake_screen.fill('black')
        fake_screen.blit(pic, (100, 100))
        screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()
    
main()   