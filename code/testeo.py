# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Configuración de la pantalla
# # ANCHO_INICIAL = 800
# # ALTO_INICIAL = 600
# # ventana = pygame.display.set_mode((ANCHO_INICIAL, ALTO_INICIAL), pygame.RESIZABLE)
# # pygame.display.set_caption('Juego Redimensionable')

# # # Colores
# # BLANCO = (255, 255, 255)
# # ROJO = (255, 0, 0)
# # AZUL = (0, 0, 255)

# # # Fuente para el texto
# # fuente = pygame.font.SysFont(None, 36)

# # # Posiciones originales y dimensiones de los elementos
# # elementos = {
# #     "boton_jugar": {
# #         "rect": pygame.Rect(100, 100, 200, 50),
# #         "color": AZUL,
# #         "text": "Jugar",
# #     },
# #     "caja_texto": {
# #         "rect": pygame.Rect(400, 300, 300, 100),
# #         "color": ROJO,
# #         "text": "Texto",
# #     }
# # }

# # # Guardar las posiciones y dimensiones originales
# # elementos_originales = {
# #     key: elem["rect"].copy() for key, elem in elementos.items()
# # }

# # # Función para redimensionar elementos proporcionalmente
# # def redimensionar_elementos(nueva_ventana, elementos, elementos_originales):
# #     ancho_ventana, alto_ventana = nueva_ventana.get_size()
    
# #     for key, elem in elementos.items():
# #         rect_original = elementos_originales[key]
# #         rect = elem["rect"]
        
# #         # Escalar la posición y dimensiones de los elementos proporcionalmente
# #         rect.x = int(rect_original.x * ancho_ventana / ANCHO_INICIAL)
# #         rect.y = int(rect_original.y * alto_ventana / ALTO_INICIAL)
# #         rect.width = int(rect_original.width * ancho_ventana / ANCHO_INICIAL)
# #         rect.height = int(rect_original.height * alto_ventana / ALTO_INICIAL)

# # # Función para restaurar las posiciones y dimensiones originales
# # def restaurar_elementos(elementos, elementos_originales):
# #     for key in elementos:
# #         elementos[key]["rect"] = elementos_originales[key].copy()

# # # Bucle principal del juego
# # def main():
# #     flag_run = True

# #     while flag_run:
# #         for evento in pygame.event.get():
# #             if evento.type == pygame.QUIT:
# #                 flag_run = False
# #             elif evento.type == pygame.VIDEORESIZE:
# #                 nueva_ventana = pygame.display.set_mode(evento.size, pygame.RESIZABLE)
# #                 redimensionar_elementos(nueva_ventana, elementos, elementos_originales)
# #                 # Restaurar si el tamaño es el original
# #                 if evento.size == (ANCHO_INICIAL, ALTO_INICIAL):
# #                     restaurar_elementos(elementos, elementos_originales)

# #         ventana.fill(BLANCO)

# #         # Dibujar elementos
# #         for key, elem in elementos.items():
# #             pygame.draw.rect(ventana, elem["color"], elem["rect"])
# #             text_surface = fuente.render(elem["text"], True, BLANCO)
# #             text_rect = text_surface.get_rect(center=elem["rect"].center)
# #             ventana.blit(text_surface, text_rect)

# #         pygame.display.update()

# #     pygame.quit()
# #     sys.exit()

# # if __name__ == "__main__":
# #     main()


# # import pygame
# # from pygame.locals import *

# # def main():
# #     pygame.init()
# #     screen = pygame.display.set_mode((200, 200),HWSURFACE|DOUBLEBUF|RESIZABLE)
# #     fake_screen = screen.copy()
# #     pic = pygame.surface.Surface((50, 50))
# #     pic.fill((255, 100, 200))

# #     while True:
# #         for event in pygame.event.get():
# #             if event.type == QUIT: 
# #                 pygame.display.quit()
# #             elif event.type == VIDEORESIZE:
# #                 screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

# #         fake_screen.fill('black')
# #         fake_screen.blit(pic, (100, 100))
# #         screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
# #         pygame.display.flip()
    
# # main()   

# # import pygame

# # pygame.init()

# # # Font constants
# # ARIALNARROW_40 = font = pygame.font.Font(r"code\data\vinque rg.otf", 40)
# # ARIALNARROW_42 = font = pygame.font.Font(r"code\data\vinque rg.otf", 42)

# # # Screen size
# # WIDTH = 900
# # HEIGHT = 600

# # def text_speech(font, text, color, x, y, bold):
# #     font.set_bold(bold)
# #     rendered_text = font.render(text, True, color)

# #     # Directly center the rect upon its creation
# #     text_rect = rendered_text.get_rect(center=(x,y))
# #     return text_rect, rendered_text

# # screen = pygame.display.set_mode((WIDTH, HEIGHT))

# # inner_rect, inner_text = text_speech(
# #     ARIALNARROW_40, 'Hello', (255, 255, 255),
# #     (WIDTH / 2), (HEIGHT / 2), False
# # )

# # # For your outline
# # outline_rect, outline_text = text_speech(
# #     ARIALNARROW_42, 'Hello', (255, 0, 0),
# #     (WIDTH / 2), (HEIGHT / 2), False
# # )

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             exit()


# #     # Paint our screen
# #     screen.fill((0,0,0))

# #     if inner_rect.collidepoint(pygame.mouse.get_pos()):
# #         # Touching our text! Render outline
# #         screen.blit(outline_text, outline_rect)

# #     screen.blit(inner_text, inner_rect)


# #     # Enact our display changes
# #     pygame.display.update()

# import os, sys, pygame, pygame.font, pygame.image
# from pygame.locals import *


# def textHollow(font, message, fontcolor):
#     notcolor = [c^0xFF for c in fontcolor]
#     base = font.render(message, 0, fontcolor, notcolor)
#     size = base.get_width() + 2, base.get_height() + 2
#     img = pygame.Surface(size, 16)
#     img.fill(notcolor)
#     base.set_colorkey(0)
#     img.blit(base, (0, 0))
#     img.blit(base, (2, 0))
#     img.blit(base, (0, 2))
#     img.blit(base, (2, 2))
#     base.set_colorkey(0)
#     base.set_palette_at(1, notcolor)
#     img.blit(base, (1, 1))
#     img.set_colorkey(notcolor)
#     return img

# def textOutline(font, message, fontcolor, outlinecolor):
#     base = font.render(message, 0, fontcolor)
#     outline = textHollow(font, message, outlinecolor)
#     img = pygame.Surface(outline.get_size(), 16)
#     img.blit(base, (1, 1))
#     img.blit(outline, (0, 0))
#     img.set_colorkey(0)
#     return img


# entry_info1 = 'Hollow, by Pete Shinners'
# entry_info2 = 'Outlined, by Pete Shinners'

# #this code will display our work, if the script is run...
# if __name__ == '__main__':
#     pygame.init()

#     #create our fancy text
#     white = 255, 255, 255
#     grey = 100, 100, 100
#     bigfont = pygame.font.Font(None, 60)
#     text1 = textHollow(bigfont, entry_info1, white)
#     text2 = textOutline(bigfont, entry_info2, grey, white)

#     #create a window the correct size
#     width = max(text1.get_width(), text2.get_width())
#     height = text1.get_height() + text2.get_height()
#     win = pygame.display.set_mode((width, height))
#     win.fill((20, 20, 80), (0, 0, width, 30))
#     win.fill((20, 20, 80), (0, height-30, width, 30))

#     win.blit(text1, (0, 0))
#     win.blit(text2, (0, text1.get_height()))
#     pygame.display.flip()
    
#     #wait for the finish
#     while 1:
#         event = pygame.event.wait()
#         if event.type is KEYDOWN and event.key == K_s: #save it
#             name = os.path.splitext(sys.argv[0])[0] + '.bmp'
#             pygame.image.save(win, name)
#         elif event.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
#             break


# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# Why is alpha blending not working properly?
# https://stackoverflow.com/questions/54342525/why-is-alpha-blending-not-working-properly-pygame/54348618#54348618
#
# GitHub - PyGameExamplesAndAnswers - vBlending and transparency - Blending
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_blending_and_transaprency.md

# import pygame

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((600, 600), 0, 32)

# def transparentSurface(size):
#     surface = pygame.Surface(screen.get_size()).convert_alpha()
#     surface.fill((0, 0, 0, 0))
#     return surface

# alpha, increase = 0, 1
# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     screen.fill(pygame.Color(247, 25, 0,255))
    
#     alpha_surface1 = transparentSurface(screen.get_size())
#     pygame.draw.rect(alpha_surface1, (247, 137, 0, 255), (120, 120, 480, 480))

#     alpha_surface2 =  transparentSurface(screen.get_size())
#     pygame.draw.rect(alpha_surface2, (220, 247, 0, alpha), (240, 240, 360, 360))

#     alpha_surface3 =  transparentSurface(screen.get_size())
#     pygame.draw.rect(alpha_surface3, (0, 247, 4), (360, 360, 240, 240) )

#     alpha_surface4 =  transparentSurface(screen.get_size())
#     pygame.draw.rect(alpha_surface4, (0, 78, 247, alpha), (480, 480, 120, 120) )
    
#     screen.blit(alpha_surface1, (0,0))
#     screen.blit(alpha_surface2, (0,0))
#     screen.blit(alpha_surface3, (0,0))
#     screen.blit(alpha_surface4, (0,0))

#     pygame.display.flip()
    
#     alpha += increase
#     if alpha < 0 or alpha > 255:
#         increase *= -1
#         alpha = max(0, min(255, alpha))

# pygame.quit()
# exit()

# import pygame
# import time
# from PIL import Image

# # Inicializar Pygame
# pygame.init()

# # Configurar ventana
# window_size = (800, 600)
# window = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Cursor Animado con GIF")

# # Cargar GIF y descomponer en fotogramas usando PIL
# gif_path = r'code\data\「无」.gif'
# gif = Image.open(gif_path)

# frames = []
# try:
#     while True:
#         frame = gif.copy()
#         frames.append(frame)
#         gif.seek(gif.tell() + 1)
# except EOFError:
#     pass

# # Convertir cada fotograma a una superficie de Pygame
# cursor_frames = [pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode).convert_alpha() for frame in frames]

# # Índice actual del fotograma del cursor
# current_frame = 0
# # Tiempo entre cambios de fotograma (en milisegundos)
# frame_time = gif.info.get('duration', 100)  # Duración del fotograma (predeterminado: 100ms si no está presente)
# # Reloj para medir el tiempo
# clock = pygame.time.Clock()
# # Tiempo acumulado
# time_accumulated = 0

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.mouse.set_visible(False)
#     # Obtener la posición actual del mouse
#     mouse_pos = pygame.mouse.get_pos()

#     # Actualizar el índice del fotograma del cursor basado en el tiempo acumulado
#     time_accumulated += clock.get_time()
#     if time_accumulated >= frame_time:
#         current_frame = (current_frame + 1) % len(cursor_frames)
#         time_accumulated = 0

#     # Dibujar fondo
#     window.fill((255, 255, 255))

#     # Dibujar el cursor animado en la posición del mouse
#     window.blit(cursor_frames[current_frame], mouse_pos)

#     # Actualizar pantalla
#     pygame.display.flip()

#     # Mantener el framerate
#     clock.tick(60)

# pygame.quit()

# import pygame
# import constantes

# # Inicializar Pygame
# pygame.init()

# # Configuración de la pantalla
# screen_width = 1280
# screen_height = 720
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Botones y Colisiones")

# # Colores
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)

# # Definir botones como rectángulos
# button1 = pygame.Rect(100, 500, 150, 50)
# button2 = pygame.Rect(300, 300, 150, 50)
# mucho_texto = (
# "Pop the Card es un juego de descubrir las palabras. Se te daran 6 letras, con\n"
# "las cuales deberás formar la mayor cantidad de palabras posibles, sin repetir\nlas letras."
# "\nLas palabras a encontrar estarán compuestas de 3, 4, 5 y 6 caracteres, y cada\n"
# "partida durará 90 segundos, debiendo jugar por lo menos 3 partidas para\npoder guardar tu puntaje."
# )

# fuente = pygame.font.Font(r"code\data\vinque rg.otf", 36)

# def render_multi_line(screen, text, x, y, font_size, color):
#     lines = text.splitlines()
#     for i, l in enumerate(lines):
#         screen.blit(fuente.render(l, 0, color), (x, y + font_size * i))


# # Bucle principal del juego
# running = True
# texto = False
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if button1.collidepoint(event.pos):
#                 print("Botón 1 presionado")
#                 texto = True
#             if button2.collidepoint(event.pos):
#                 print("Botón 2 presionado")
#                 texto = False

#     # Rellenar la pantalla con un color de fondo
#     screen.fill("aquamarine4")

#     render_multi_line(screen, mucho_texto, 10, 10, 50, "black")

#     # Dibujar los botones
#     # pygame.draw.rect(screen, BLUE, button1)
#     # pygame.draw.rect(screen, RED, button2)

#     # Actualizar la pantalla
#     pygame.display.flip()

# # Salir de Pygame
# pygame.quit()

from constantes import *
from class_box import Box


menu_salir = {
              "box": Box((1280, 720), (100,540), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, True, 5],
              "text": ["Salir", LETRAS_2, FUENTE_1, 60, "shadow", 1, BORDE_2, True]
              }

menu_jugar = {
              "box": Box((1280, 720), (100,300), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, True, 5],
              "text": ["Jugar", LETRAS_2, FUENTE_1, 60, "shadow", 1, BORDE_2, True]
              }

menu_options = {
              "box": Box((1280, 720), (100,420), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, True, 5],
              "text": ["Opciones", LETRAS_2, FUENTE_1, 60, "shadow", 1, BORDE_2, True]
              }


MENU_LISTA = [menu_jugar, menu_salir, menu_options]

print(menu_jugar["colors"][0], menu_jugar["colors"][1], menu_jugar["colors"][2])