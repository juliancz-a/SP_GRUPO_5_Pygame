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

        self.cards = 6

        self.music = music_file
        self.background = r"code\data\img\newbg.png"

    def render(self):

        self.menu_button.set_color("red", "yellow", "grey")
        menu = False
        Play.set_music(self)

        letras_seleccionadas = []
        card_list = []
        empty_card_list = []

        card_list = set_cards(card_list, self.original_wh, self.cards, 100)
        empty_card_list = set_cards(empty_card_list, self.original_wh, self.cards, 250)

        self.menu_button.resize((self.surface.get_size()))

        cards_resize((self.surface.get_size()), card_list)

        append = 0
        pos = 0
        p_list = [0,1,2,3,4,5]
        free_spaces = []


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

                #elif evento.type == pygame.JOIN

                menu = self.menu_button.interaction(event)
                pos = set_cards_interaction(event, card_list, letras_seleccionadas, p_list, free_spaces)

                # if event.type == move_card:
                #     draw_cards(self.surface, letras_seleccionadas, )


            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            draw_empty_cards(self.surface, card_list, empty_card_list, letras_seleccionadas, append)
            draw_cards(self.surface, card_list, letras)

            self.menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.menu_button.draw_text(self.surface, "Volver al menú", "white", FUENTE_1, 40)

            pygame.display.update()


    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)


def set_cards(card_list, wh, cards_counter, y) -> list:

    center = wh[0] // 2 #x // 2 (1280 // 2)

    initial_pos_x = -315
    card_pos = 0
    for i in range(cards_counter):
        card = Box(wh,(initial_pos_x + center,y), (100,128), image=CARTAS, press_sound=CARTAS_SOUND, card_pos = card_pos)
        card_list.append(card)


        initial_pos_x += 105
        card_pos +=1

    return card_list

def draw_cards(surface:pygame.Surface, card_list:list[Box], letras):
    letras = letras.split(",")
    pos = 0

    for i in range (len(card_list)):
        card_list[i].draw_image(surface)
        card_list[i].draw_text(surface, letras[i], (255,255,255), FUENTE_2, 86, border=True, border_thickness=2)

        card_list[i].assign_letter(letras[i])
        pos += 1

def draw_empty_cards(surface:pygame.Surface, card_list:list[Box], empty_card_list:list[Box], letras:list, append):
    for i in range (len(card_list)):
        empty_card_list[i].draw_image(surface, transparency=75)

        # print(card_list[i].rectangulo)
        if len(letras) > 0 and append < len(letras):
            # print(card_list[i].rectangulo)
            #arreglar indice
            # card_list[i].rectangulo.y = 250
            # empty_card_list[i].rectangulo.y = 100
            append += 1
    return append

def set_cards_interaction(event, card_list:list[Box], selected_letters:list, position_list, free_spaces):
    occurrences_list = []
    for card in card_list:
        occurrences_list.append(card.letter)
    for card in card_list:
        action = card.interaction(event)
        if action:
            occurrences = occurrences_list.count(card.letter)

            if selected_letters.count(card.letter) < occurrences and not card.append:

                selected_letters.append(card.letter)
                card.check_append(True)

                if position_list:
                    pos = position_list[0]
                    position_list.pop(0)
                else:
                    pos = len(selected_letters) - 1

                print(f"lista posiciones : {position_list}")

                card.rectangulo.x, card.rectangulo.y = card_list[pos].original_rectangulo.x, 250

                
                free_spaces.append(card.pos)
                card.pos = pos
                
            elif card.append:

                selected_letters.remove(card.letter)
                position_list.append(card.pos)
                position_list.sort()

                print(f"espacios libres: {free_spaces}")
                card.pos = free_spaces[random.randint(0, len(free_spaces) - 1)]
                free_spaces.remove(card.pos)
                
                card.check_append(False)


                card.rectangulo.x, card.rectangulo.y = card_list[card.pos].original_rectangulo.x, 100


                #puede servir tambien
                # print(card.letter)
                # selected_letters.remove(card.letter)
                # card.reset_position()
                # card.check_append(False)


def cards_resize(event, card_list:list[Box]):
    for card in card_list:
        print(card.rectangulo.x, card.rectangulo.y)
        card.resize(event)

def change_card_pos (selected_card:Box, card_list):
    selected_card.rectangulo


# class Card:
#     def __init__(self, wh, pos, size) -> None:
#         self.pos = pos
#         self.size = size
#         self.press_sound = CARTAS_SOUND
#         self.image = CARTAS

#         self.box_card = Box(wh, self.pos, self.size, self.press_sound, self.press_sound)

# lista = ["M", "A", "L", "O"]

# x = "".join(lista)
# x = x.lower()

# print(x)