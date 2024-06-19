import pygame
from constantes import *
from class_box import Box

class Play:
    def __init__(self, surface:pygame.Surface, music_file = None) -> None:
        self.surface = surface
        self.menu_button = Box(surface.get_size(),(400,300), (200,100))
        self.play_title = Box(surface.get_size(),(200,50), (400,50))

        self.cards = 6 

        self.music = music_file
        self.background = PLAY_BACKGROUND_1
        
    def render(self):

        self.menu_button.set_color("red", "yellow", "grey")
        menu = False
        Play.set_music(self)
        card_list = set_cards(self.surface, self.cards)

        while True:
            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            if menu:
                return "menu"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.VIDEORESIZE:
                    
                    self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                    self.menu_button.resize(event.size)
                    self.play_title.resize(event.size)
                    cards_resize(event, card_list)

                menu = self.menu_button.interaction(event)
                set_cards_interaction(event, card_list)



            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            draw_cards(self.surface, card_list)

            self.menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.menu_button.draw_text(self.surface, "Volver al menú", "white", FUENTE_1, 30)

            self.play_title.draw_text(self.surface, "A jugar!", "red", FUENTE_1, 50)
            pygame.display.update()

    
    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        
    
def set_cards(surface, cards_counter:Box) -> list:
    card_list = []
    initial_pos_x = 50
    for i in range(cards_counter):
        card = Box(surface.get_size(),(initial_pos_x,400), (100,128), image=r"code\data\img\card_example.png", press_sound=r"code\data\sound\card_click.wav")
        card_list.append(card)
        initial_pos_x += 105
    
    return card_list

def draw_cards(surface, card_list):
    for card in card_list:
        card.draw_image(surface)

def set_cards_interaction(event, card_list):
    for card in card_list:
        card.interaction(event)

def cards_resize(event, card_list):
    for card in card_list:
        card.resize(event.size)