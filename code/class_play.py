import pygame
from constantes import *
from class_box import Box

from data.config.config import *
import random


lista = read_data(r"code\data\config\palabras.json")
combinaciones = list(lista[0].items())


palabra_secretita = random.choice(combinaciones)

letras = palabra_secretita[0]
print(letras)
palabras_a_encontrar = palabra_secretita[1]

class Play:
    def __init__(self, wh, surface:pygame.Surface, music_file = None) -> None:
        self.surface = surface
        self.original_wh = wh
        self.menu_button = Box(wh,(1160,650), (100,50))
        # self.play_title = Box(wh,(200,50), (400,50))

        self.cards = 6 

        self.music = music_file
        self.background = PLAY_BACKGROUND_1
        
    def render(self):

        self.menu_button.set_color("red", "yellow", "grey")
        menu = False
        Play.set_music(self)

        card_list = set_cards(self.original_wh, self.cards, 100)
        empty_card_list = set_cards(self.original_wh, self.cards, 250)

        letras_seleccionadas = []

        self.menu_button.resize((self.surface.get_size()))
    
        cards_resize((self.surface.get_size()), card_list)

        while True:
            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            if menu:
                return "menu", self.original_wh

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.VIDEORESIZE:

                    self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                    self.menu_button.resize(event.size)
                    # self.play_title.resize(event.size)
                    cards_resize(event.size, card_list)

                menu = self.menu_button.interaction(event)
                set_cards_interaction(event, card_list, letras_seleccionadas)

            if len(letras_seleccionadas) > 0 :
                print(letras_seleccionadas)

            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            draw_cards(self.surface, card_list, letras)
            draw_empty_cards(self.surface, empty_card_list, letras_seleccionadas)

            self.menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.menu_button.draw_text(self.surface, "Volver al menú", "white", FUENTE_1, 40)

            # self.play_title.draw_text(self.surface, "A jugar!", "red", FUENTE_1, 50)
            pygame.display.update()

    
    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        
    
def set_cards(wh, cards_counter, y) -> list:

    center = wh[0] // 2 #x // 2 (1280 // 2)

    card_list = []
    initial_pos_x = -315
    for i in range(cards_counter):
        card = Box(wh,(initial_pos_x + center,y), (100,128), image=CARTAS, press_sound=CARTAS_SOUND)
        card_list.append(card)
            
        initial_pos_x += 105
    
    return card_list

def draw_cards(surface:pygame.Surface, card_list:list[Box], letras):
    letras = letras.split(",")

    for i in range (len(card_list)):
        card_list[i].draw_image(surface)
        card_list[i].draw_text(surface, letras[i], (255,255,255), FUENTE_2, 86, border=True, border_thickness=2)

        card_list[i].assign_letter(letras[i])

def draw_empty_cards(surface:pygame.Surface, card_list:list[Box], letras):
    for i in range (len(card_list)):
        card_list[i].draw_image(surface, transparency=75)

        # if letras != None:
        #     card_list[i].draw_text(surface, letras[i], "black", FUENTE_1, 100)

def set_cards_interaction(event, card_list:list[Box], selected_letters):
    for card in card_list:
        action = card.interaction(event)
        if action:
            occurrences = card_list.count(card.letter)
            if selected_letters.count(card.letter) <= occurrences:
                selected_letters.append(card.letter)

    

def cards_resize(event, card_list:list[Box]):
    for card in card_list:
        print(card.rectangulo.x, card.rectangulo.y)
        card.resize(event)

