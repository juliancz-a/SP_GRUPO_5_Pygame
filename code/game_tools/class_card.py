from game_tools.class_image import * 
from game_tools.class_box import *
from game_tools.extra_functions import *

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