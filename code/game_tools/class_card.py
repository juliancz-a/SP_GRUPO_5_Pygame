from game_tools.class_image import * 
from game_tools.class_box import *
from game_tools.extra_functions import *

class Card:

    def __init__(self, dimensiones:tuple, coords:tuple, image_path:str, press_sound:str, card_pos:int, card_letter:str = None) -> None:       
        """Creación de objeto tipo Card (carta) para su interacción, movimiento y renderización. Comparte las propiedades de un objeto del tipo Image

        Args:
            dimensiones (tuple): Dimensiones del objeto
            coords (tuple): Coordenadas del objeto, deben estar dentro de una superficie
            image_path (str): Ruta de la imagen del objeto
            press_sound (str): Ruta del sonido del objeto al presionarlo
            card_pos (int): Posicion del objeto con respecto a los demás objetos del mismo tipo
            card_letter (str, optional): Letra del objeto
        """

        self.letter = card_letter
        self.card_pos = card_pos
        self.append = False

        self.card_image = Image(image_path, coords, dimensiones, press_sound= press_sound)
        self.card_box = self.card_image.image_box

    def draw_card(self, surface:pygame.Surface, letter_color:str, font:str, font_size:int, transparency:int = 255):
        """Dibujar en pantalla una carta.

        Args:
            surface (pygame.Surface): Superficie sobre la cual realizar el dibujo.
            letter_color (_type_): Color de la letra perteneciente a la carta
            font (str): Fuente de la letra.
            font_size (int): Tamaño de la fuente de la letra.
            transparency (int, optional): Transparencia de la carta (imagen)
        """
        self.card_image.draw_image(surface, transparency)
        self.card_box.draw_text(surface, self.letter, letter_color, font, font_size, outline="border", outline_thickness=2, center=True)