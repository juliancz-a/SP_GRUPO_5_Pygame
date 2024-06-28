from class_image import * 
from class_box import *

class Card:

    def __init__(self, dimensiones, coords, image_path, press_sound, card_pos, card_letter = None) -> None:


        self.letter = card_letter
        self.card_pos = card_pos
        self.append = False

        self.card_image = Image(image_path, coords, dimensiones, press_sound= press_sound)
        self.card_box = self.card_image.image_box

    def draw_card(self, surface:pygame.Surface, letter_color, font, font_size, transparency = 255):
    
        self.card_image.draw_image(surface, transparency)
        self.card_box.draw_text(surface, self.letter, letter_color, font, font_size, outline="border", outline_thickness=2, center=True)
    
    # def move_card(self, destino, velocidad):
    #     velocidad = 1
    #     x = velocidad
    #     y = velocidad

    #     while self.card_box.rectangulo.y < destino[1]:
    #         self.card_box.rectangulo.y += x
    #     # else:
    #     #     self.card_box.rectangulo.y = destino[1]
            
    #     while self.card_box.rectangulo.x < destino[0]:
    #         self.card_box.rectangulo.x += y
    #     # else:
    #     #     self.card_box.rectangulo.y = destino[0]
