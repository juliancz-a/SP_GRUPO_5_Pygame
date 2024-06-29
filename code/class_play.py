import pygame
from constantes import *
from class_box import Box
from class_image import Image
from class_card import Card

from draw_functions import *

from data.config.config import *
import random


class Play:
    def __init__(self, surface:pygame.Surface, match, lista, score, comodin, music_file = None ) -> None:

        self.surface = surface
        self.match = match
        #BOTONES
        self.menu_button = Box((1160,650), (100,50))
        self.join_button = Box((750,420), (80,50))
        self.comodin_button = Image(COMODIN, (1070, 220), (100,100), image_hover_path=COMODIN_HOVER,  press_sound=PRESS_COMODIN_SOUND)
        self.clear_button = Box((200, 200), (80, 50))
        self.shuffle_button = Box((200, 265), (80, 50))
        #TEXTO
        self.timer = Box((630, 410), (50,50)) 
        self.initial_time = pygame.time.get_ticks()

        self.score = score
        self.score_text = Box((400, 410), (100,50))
    
        self.music = music_file
        #IMG
        self.background = PLAY_BACKGROUND_1

        #CARDS
        datos_palabras = set_combination(lista)
        self.combinaciones = datos_palabras[1]
        self.letras = datos_palabras[0]
        self.matriz_combinaciones = normalize_words(self.combinaciones)

        self.cards_cfg = {"cards_quantity" : 6,
                          "card_list" : set_cards((self.surface.get_width(),100), 6, self.letras),
                          "empty_card_list" : set_cards((self.surface.get_width(), 250), 6),
                          "selected_letters" : ["", "", "", "", "", ""],
                          "founded_words" : [],
                          "pos_libres" : [0,1,2,3,4,5],
                          "pos_ocupadas" : []}

        self.comodin = comodin
        self.random_letter = None

        self.option = None

    def render(self):


        self.menu_button.set_color("red", "yellow", "grey")
        self.join_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        self.clear_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        self.shuffle_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        
        menu = False
    
        join = False
        
        tiempo_transcurrido = (pygame.time.get_ticks() - self.initial_time) // 1000
        tiempo_restante = TIEMPO_LIMITE - tiempo_transcurrido

        if tiempo_restante == 0:
            self.option = 1

        background = pygame.image.load(self.background)
        background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
        
        self.surface.fill("black")
        self.surface.blit(background, (0,0))

        draw_cards(self.surface, self.cards_cfg["empty_card_list"], transparency=155)
        draw_cards(self.surface, self.cards_cfg["card_list"])

        if count_select_letters(self.cards_cfg["selected_letters"]) > 2:
            self.join_button.draw_box(self.surface, 10, 5)
            self.join_button.draw_text(self.surface, "¡Unir!", "navy", FUENTE_1, 60, center=True)

        self.menu_button.draw_box(self.surface, border_radius=5, border_width=5)
        self.menu_button.draw_text(self.surface, "Volver al menú", "white", FUENTE_1, 40, center=True)

        self.clear_button.draw_box(self.surface, border_radius=5, border_width=5)
        self.clear_button.draw_text(self.surface, "CLEAR", "white", FUENTE_1, 40, center=True)

        self.shuffle_button.draw_box(self.surface, border_radius=5, border_width=5)
        self.shuffle_button.draw_text(self.surface, "SHUFFLE", "white", FUENTE_1, 40, center=True)

        
        self.timer.draw_text(self.surface, str(tiempo_restante), "white", FUENTE_4, font_size=275, center=True,outline="shadow", outline_thickness=2)

        self.score_text.draw_text(self.surface, f"Puntaje: {str(self.score)}", "darkslateblue", FUENTE_4, font_size=125, center=True,outline="shadow", outline_thickness=2)

        draw_words(self.surface, self.matriz_combinaciones, self.cards_cfg["founded_words"], self.comodin, self.random_letter)

        self.comodin_button.draw_image(self.surface)
        pygame.display.update()

    def handle_event (self, event):
        score = 0
        JOIN_CARDS = pygame.USEREVENT + 1

        if event.type == JOIN_CARDS:
            word = join_cards(self.cards_cfg["selected_letters"], self.cards_cfg["founded_words"], self.combinaciones)
            if word != False:
                self.cards_cfg["founded_words"].append(word)
                reset_pos(self.cards_cfg["card_list"], self.cards_cfg["selected_letters"], self.cards_cfg["pos_ocupadas"], self.cards_cfg["pos_libres"])
                self.score += sum_score(score, word)

        elif count_select_letters(self.cards_cfg["selected_letters"]) > 2:
            join = self.join_button.interaction(event)
            if join:
                pygame.event.post(pygame.event.Event(JOIN_CARDS))

        menu = self.menu_button.interaction(event)
        if menu:
            self.option = 0
        set_cards_interaction(event, self.cards_cfg["card_list"], self.cards_cfg["selected_letters"], self.cards_cfg["pos_libres"], self.cards_cfg["pos_ocupadas"])
        if self.comodin == 1:
            action = self.comodin_button.image_box.interaction(event)
            
            if action:
                self.comodin = 0
                self.random_letter = select_random_letter(self.combinaciones)

        if self.clear_button.interaction(event):
            reset_pos(self.cards_cfg["card_list"], self.cards_cfg["selected_letters"], self.cards_cfg["pos_ocupadas"], self.cards_cfg["pos_libres"])
        
        if self.shuffle_button.interaction(event):
            shuffle(self.cards_cfg["card_list"])

    def update(self):
       
        selection = None

        match self.option:
            case 0:
                selection = "menu"
            case 1:
                selection = "finish_match"

        return selection
    
    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
    
    def update_play_instance (self):
        self.match += 1
        
        data = self.match, self.score

        return data
    
def set_cards(coords, cards_counter, letras = None) -> list:
    card_list = []
    x = coords[0]
    y = coords[1]

    center = x // 2 
    if letras != None:
        letras = letras.split(",")

    initial_pos_x = -315
    card_pos = 0

    for i in range(cards_counter):
        
        card = Card( (100,128), (initial_pos_x + center,y), CARTAS, CARTAS_SOUND, card_pos)
        if letras != None:
            card.letter = letras[i]
        card_list.append(card)

        initial_pos_x += 105
        card_pos +=1

    return card_list

def draw_cards(surface:pygame.Surface, card_list:list[Card], transparency = 255):

    for i in range (len(card_list)):
        card_list[i].draw_card(surface, COLOR_LETRAS, FUENTE_2, 86, transparency)


def set_cards_interaction(event, card_list:list[Card], selected_letters:list, position_list, free_spaces):
    occurrences_list = []
    for card in card_list:
        occurrences_list.append(card.letter)
    for card in card_list:
        action = card.card_box.interaction(event)
        if action:
            occurrences = occurrences_list.count(card.letter)

            if selected_letters.count(card.letter) < occurrences and not card.append:

                pos = position_list[0]
                position_list.pop(0)
            
                selected_letters[pos] = card.letter
                print(position_list)
                card.append = True
               
                card.card_box.rectangulo.x, card.card_box.rectangulo.y = card_list[pos].card_box.original_rectangulo.x, 250
                
                free_spaces.append(card.card_pos)
                card.card_pos = pos
                
            elif card.append:
                return_card(card_list, card, selected_letters, free_spaces, position_list)


def reset_pos (card_list:list[Box], selected_letters:list, free_spaces, position_list:list):
    for card in card_list:
        if card.append:
            return_card(card_list, card, selected_letters, free_spaces, position_list)


def return_card (card_list:list[Box], card, selected_letters:list, free_spaces, position_list:list):

    selected_letters[card.card_pos] = ""
    position_list.append(card.card_pos)
    position_list.sort()

    card.card_pos = free_spaces[len(free_spaces) - 1]
    free_spaces.remove(card.card_pos)
    
    card.append = False

    card.card_box.rectangulo.x, card.card_box.rectangulo.y = card_list[card.card_pos].card_box.original_rectangulo.x, 100


def join_cards (selected_letters:list, words_founded:list, combinaciones):
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

def draw_words (surface, matrix, words_founded:list, comodin, random_letter):
    
    x = 55
    
    for i in range (len(matrix)):
        printed = 0
        y = 530
        x += 100
        for j in range (len(matrix[i])):

            if printed == 6 and j != len(matrix[i]) - 1:
                y = 530
                x += 100
                printed = 0

            elif j == len(matrix[i]) - 1 and printed == 6:
                printed = 0

            if matrix[i][j] != 0:
                word = matrix[i][j]
                word_text = word
                word = Box((x, y), (40, 100))

                if comodin == 0:
                    letter = use_comodin(random_letter, words_founded, word_text)
                    if letter[0] != False:
                        letter_box = Box((x + letter[1],y), (40,100))

                        letter_box.draw_text(surface, letter[0], COLOR_PALABRA, FUENTE_3, font_size=200, outline="shadow")

                for word_founded in words_founded:
                    if word_founded == matrix[i][j]:
                        word.draw_text(surface,word_text, COLOR_PALABRA, FUENTE_3, font_size=200, outline="shadow")
                        break
        
                word.draw_text(surface,f"_"*(6-i), COLOR_PALABRA, FUENTE_3, font_size=250)
                
                y += 20
                printed +=1

def sum_score(scoreboard:int, word):
    scoreboard += len(word)
    return scoreboard

def normalize_words (combinations):
    palabras = {3: [], 4: [], 5: [], 6: []}

    for combination in combinations:
        for key in palabras.keys():
            if len(combination) == key:
                palabras[key].append(combination)

    max_len = ordenar_elementos([len(palabras[3]), len(palabras[4]), len(palabras[5]), len(palabras[6])], 1)

    matriz = [[0] * max_len for _ in range(4)]

    for i in range (len(matriz)):
        for j in range (len(palabras[6-i])):
                matriz[i][j] = palabras[6-i][j]
    print(matriz)

    return matriz

    
def ordenar_elementos (list:list[dict], orden:int):

    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            match orden:
                case 1:
                    if list[i] >= list[j]:
                            swap(list, i, j)
                case 2:
                    if list[i] <= list[j]:
                        swap(list, i, j)
    return list.pop()

def swap(list:list[dict], a:int, b:int):
    aux = list[a]
    list[a] = list[b]
    list[b] = aux

def select_random_letter (combinaciones):


    elemento_random = random.randint(0, len(combinaciones) - 1)
    palabra = combinaciones[elemento_random]
    
    letra = palabra[random.randint(0, len(palabra) - 1)]

    return letra

def use_comodin (letter, words_founded, word_text):
    pos = 0
    coincidence = False
    for matrix_letter in word_text:
        if matrix_letter == letter:
            coincidence = True
            break
        pos += 12

    for word_founded in words_founded:
        if word_founded == word_text:
            coincidence = False

    if coincidence == False:
        letter, pos = False, False
    return letter,pos

def count_select_letters (selected_letters:list) -> int:
    count = 0
    for letter in selected_letters:
        if letter != "":
            count += 1
    
    return count

def set_combination (lista:list[dict]) -> tuple:
    #key, values
    lista_letras = list(lista[0].keys())
    letras = random.choice(lista_letras)

    combinaciones = lista[0].pop(letras)

    datos = letras, combinaciones

    return datos


def shuffle (card_list):
    shuffle_card = []
    for card in card_list:
        print(card.letter)
        if card.append is False:
            shuffle_card.append(card.letter)
    for card in card_list:
        if card.append is False:
           
            card.letter = shuffle_card.pop(random.randint(0, len(shuffle_card) - 1))
        print(card.letter)
