import pygame
from constantes import *
from class_box import Box

from data.config.config import *
import random


lista = read_data(r"code\data\config\palabras.json")
combinaciones = list(lista[0].keys())


palabra_secretita = random.choice(combinaciones)
combinaciones = lista[0][palabra_secretita]
print(palabra_secretita)
print(combinaciones)
palabras_a_encontrar = palabra_secretita[1]

class Play:
    def __init__(self, wh, surface:pygame.Surface, music_file = None) -> None:
        self.surface = surface
        self.original_wh = wh

        self.menu_button = Box(wh,(1160,650), (100,50))
        self.join_button = Box(wh, (750,420), (80,50))
        self.timer = Box(wh, (630, 410), (50,50))

        self.cards = 6

        self.music = music_file
        self.background = r"code\data\img\newbg.png"

    def render(self):
        
        tiempo_inicio = pygame.time.get_ticks()

        self.menu_button.set_color("red", "yellow", "grey")
        self.join_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        
        menu = False
        Play.set_music(self)

        letras_seleccionadas = []
        card_list = []
        empty_card_list = []
        palabras_encontradas = []

        card_list = set_cards(card_list, self.original_wh, self.cards, 100)
        empty_card_list = set_cards(empty_card_list, self.original_wh, self.cards, 250)

        self.menu_button.resize((self.surface.get_size()))
        self.join_button.resize((self.surface.get_size()))

        cards_resize((self.surface.get_size()), card_list)

        p_list = [0,1,2,3,4,5]
        free_spaces = []
        join = False

        JOIN_CARDS = pygame.USEREVENT + 1

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
                    cards_resize(event.size, card_list)

                elif event.type == JOIN_CARDS:
                    card = join_cards(letras_seleccionadas, palabras_encontradas)
                    if card != False:
                        palabras_encontradas.append(card)
                        reset_pos(card_list, letras_seleccionadas, free_spaces, p_list)

                elif len(letras_seleccionadas) > 2:
                    join = self.join_button.interaction(event)
                    if join:
                        pygame.event.post(pygame.event.Event(JOIN_CARDS))

                menu = self.menu_button.interaction(event)
                set_cards_interaction(event, card_list, letras_seleccionadas, p_list, free_spaces)
        
            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            draw_empty_cards(self.surface, card_list, empty_card_list)
            draw_cards(self.surface, card_list, palabra_secretita)

            if len(letras_seleccionadas) >= 3:
                self.join_button.draw_box(self.surface, 10, True, 5)
                self.join_button.draw_text(self.surface, "¡Unir!", "navy", FUENTE_1, 60, center=True)

            self.menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.menu_button.draw_text(self.surface, "Volver al menú", "white", FUENTE_1, 40, center=True)

            if len(palabras_encontradas) > 0:
                draw_words(self.original_wh, self.surface, palabras_encontradas)
            
            tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000
            tiempo_restante = TIEMPO_LIMITE - tiempo_transcurrido
         
            self.timer.draw_text(self.surface, str(tiempo_restante), "white", FUENTE_4, font_size=275, center=True, shadow=True, border_thickness=2)

    
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
        card_list[i].draw_text(surface, letras[i], (255,255,255), FUENTE_2, 86, border=True, border_thickness=2, center=True)

        card_list[i].assign_letter(letras[i])
        pos += 1

def draw_empty_cards(surface:pygame.Surface, card_list:list[Box], empty_card_list:list[Box]):
    for i in range (len(card_list)):
        empty_card_list[i].draw_image(surface, transparency=75)

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

                return_card(card_list, card, selected_letters, free_spaces, position_list)

def reset_pos (card_list:list[Box], selected_letters:list, free_spaces, position_list:list):
    for card in card_list:
        if card.append:
            return_card(card_list, card, selected_letters, free_spaces, position_list)


def return_card (card_list:list[Box], card, selected_letters:list, free_spaces, position_list:list):

    selected_letters.remove(card.letter)
    position_list.append(card.pos)
    position_list.sort()

    print(f"espacios libres: {free_spaces}")
    card.pos = free_spaces[random.randint(0, len(free_spaces) - 1)]
    free_spaces.remove(card.pos)
    
    card.check_append(False)

    card.rectangulo.x, card.rectangulo.y = card_list[card.pos].original_rectangulo.x, 100


def cards_resize(event, card_list:list[Box]):
    for card in card_list:
        print(card.rectangulo.x, card.rectangulo.y)
        card.resize(event)


def join_cards (selected_letters:list, words_founded:list):
    retorno = False

    palabra = "".join(selected_letters).lower()

    set_dict = set(combinaciones)
    
    palabra_set = {palabra}

    intersec = set_dict.intersection(palabra_set)

    coincidences = words_founded.count(palabra)

    if len(intersec) > 0 and coincidences == 0:
        retorno = palabra
    else:
        retorno = False

    return retorno

def draw_words (wh, surface, words_founded:list) -> int:

    x = 165
    y = 530
    printed = 0
    for i in range (len(words_founded)):
        if printed == 6:
            y = 530
            x += 135
            printed = 0

        word = words_founded[i]
        word_text = word
        word = Box(wh, (x, y), (40, 100))
    
        word.draw_text(surface, word_text.upper(), COLOR_PALABRA, FUENTE_3, font_size=200, shadow=1)
        y += 20
        printed += 1
