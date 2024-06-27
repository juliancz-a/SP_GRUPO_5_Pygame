from class_image import * 
from class_box import *

class Card:

    def __init__(self, dimensiones, coords, image_path, press_sound, card_letter, card_pos) -> None:


        self.letter = card_letter
        self.card_pos = card_pos
        self.append = False

        self.card_image = Image(image_path, coords, dimensiones, press_sound= press_sound)

    def draw_card(self, surface:pygame.Surface, letter_color):
    
        self.card_image.draw_image(surface)
        self.card_image.image_box.draw_text(surface, self.letter, (letter_color), FUENTE_2, 86, border=True, border_thickness=2, center=True)

    
    def move_card(self):
        self.card_image.image_box.rectangulo.y +=

        self.card_image.image_box.rectangulo.x, card.rectangulo.y = card_list[pos].original_rectangulo.x, 250