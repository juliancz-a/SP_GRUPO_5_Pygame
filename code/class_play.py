import pygame
from constantes import *
from class_box import Box

from data.config.config import *
import random


class Play:
    def __init__(self, surface:pygame.Surface, match, lista, score, music_file = None ) -> None:
        self.lista = lista

        self.surface = surface
        self.match = match

        self.menu_button = Box((1160,650), (100,50))
        self.join_button = Box( (750,420), (80,50))
        self.comodin_button = Box( (1070, 220), (100,100), press_sound=PRESS_COMODIN_SOUND, image= r"code\data\img\spell_comodin.png", image_hover=r"code\data\img\spell_comodin_hover.png")
        self.clear_button = Box( (200, 200), (80, 50))
        self.shuffle_button = Box( (200, 265), (80, 50))

        self.timer = Box((630, 410), (50,50))
        self.score = score
        self.score_text = Box((400, 410), (100,50))
    
        self.cards = 6
        self.words_matrix = None
        self.music = music_file
        self.background = PLAY_BACKGROUND_1

    def render(self):
        words_data = set_combination(self.lista)
        combinaciones = words_data[1]
        palabra_secretita = words_data[0]
        self.words_matrix = normalize_words(combinaciones)

        tiempo_inicio = pygame.time.get_ticks()

        self.menu_button.set_color("red", "yellow", "grey")
        self.join_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        self.clear_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        self.shuffle_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")
        
        menu = False
        Play.set_music(self)

        letras_seleccionadas = ["", "", "", "", "", ""]
        card_list = []
        empty_card_list = []
        palabras_encontradas = []
        p_list = [0,1,2,3,4,5]
        free_spaces = []
    
        card_list = set_cards(self.surface.get_size(), card_list, self.cards, 100, palabra_secretita)
        empty_card_list = set_cards(self.surface.get_size(), empty_card_list, self.cards, 250, palabra_secretita)


        join = False
        score = 0
        activate_comodin = 0
        comodin = False
        random_letter = None
        JOIN_CARDS = pygame.USEREVENT + 1
        print(f"contador de partidas: {self.match}")
        print(f"Lista : {self.lista}, len: {len(self.lista[0])}")
        while True:
           
            tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000
            tiempo_restante = TIEMPO_LIMITE - tiempo_transcurrido

            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            
            if menu:
                return "menu"  
            if tiempo_restante == 0 or len(palabras_encontradas) == len(combinaciones):
                self.match += 1
                self.score += score
                return "finish_match"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                elif event.type == JOIN_CARDS:
                    word = join_cards(letras_seleccionadas, palabras_encontradas, combinaciones)
                    if word != False:
                        palabras_encontradas.append(word)
                        reset_pos(card_list, letras_seleccionadas, free_spaces, p_list)
                        score = sum_score(score, word)

                elif count_select_letters(letras_seleccionadas) > 2:
                    join = self.join_button.interaction(event)
                    if join:
                        pygame.event.post(pygame.event.Event(JOIN_CARDS))

                menu = self.menu_button.interaction(event)
                set_cards_interaction(event, card_list, letras_seleccionadas, p_list, free_spaces)
                if comodin is False:
                    comodin = self.comodin_button.interaction(event)

                if self.clear_button.interaction(event):
                    reset_pos(card_list, letras_seleccionadas, free_spaces, p_list)
                
                if self.shuffle_button.interaction(event):
                    shuffle(card_list, letras_seleccionadas, free_spaces, p_list)


            if comodin and activate_comodin == 0:
                random_letter = select_random_letter(combinaciones)
                activate_comodin += 1

            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            draw_empty_cards(self.surface, card_list, empty_card_list)
            draw_cards(self.surface, card_list)

            if count_select_letters(letras_seleccionadas) > 2:
                self.join_button.draw_box(self.surface, 10, True, 5)
                self.join_button.draw_text(self.surface, "¡Unir!", "navy", FUENTE_1, 60, center=True)

            self.menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.menu_button.draw_text(self.surface, "Volver al menú", "white", FUENTE_1, 40, center=True)

            self.clear_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.clear_button.draw_text(self.surface, "CLEAR", "white", FUENTE_1, 40, center=True)

            self.shuffle_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.shuffle_button.draw_text(self.surface, "SHUFFLE", "white", FUENTE_1, 40, center=True)

            
            self.timer.draw_text(self.surface, str(tiempo_restante), "white", FUENTE_4, font_size=275, center=True, shadow=True, border_thickness=2)

            self.score_text.draw_text(self.surface, f"Puntaje: {str(score)}", "darkslateblue", FUENTE_4, font_size=125, center=True, shadow=True, border_thickness=2)

            draw_words(self.surface, self.words_matrix, palabras_encontradas, comodin, random_letter)

            self.comodin_button.draw_image(self.surface)
            pygame.display.update()

    def update(self, match, score, player_list):
        score = self.score
        player_list = self.lista
        match = self.match

        data_updated = (match, score, player_list)

        return data_updated
            

    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)


def set_cards(surface_size, card_list, cards_counter, y, letras) -> list:

    center = surface_size[0] // 2 #x // 2 (1280 // 2)
    letras = letras.split(",")

    initial_pos_x = -315
    card_pos = 0
    for i in range(cards_counter):
        card = Box((initial_pos_x + center,y), (100,128), image=CARTAS, press_sound=CARTAS_SOUND, card_pos = card_pos)
        card.assign_letter(letras[i])
        card_list.append(card)


        initial_pos_x += 105
        card_pos +=1

    return card_list

def draw_cards(surface:pygame.Surface, card_list:list[Box]):
    pos = 0

    for i in range (len(card_list)):
        card_list[i].draw_image(surface)
        card_list[i].draw_text(surface, card_list[i].letter, (255,255,255), FUENTE_2, 86, border=True, border_thickness=2, center=True)

        pos += 1

def draw_empty_cards(surface:pygame.Surface, card_list:list[Box], empty_card_list:list[Box]):
    for i in range (len(card_list)):
        empty_card_list[i].draw_image(surface, transparency=100)

def set_cards_interaction(event, card_list:list[Box], selected_letters:list, position_list, free_spaces):
    occurrences_list = []
    for card in card_list:
        occurrences_list.append(card.letter)
    for card in card_list:
        action = card.interaction(event)
        if action:
            occurrences = occurrences_list.count(card.letter)

            if selected_letters.count(card.letter) < occurrences and not card.append:

                pos = position_list[0]
                position_list.pop(0)
            
                selected_letters[pos] = card.letter
                
                card.check_append(True)

                card.rectangulo.x, card.rectangulo.y = card_list[pos].original_rectangulo.x, 250
                
                free_spaces.append(card.pos)
                card.pos = pos
                
            elif card.append:
                return_card(card_list, card, selected_letters, free_spaces, position_list)


def reset_pos (card_list:list[Box], selected_letters:list, free_spaces, position_list:list, all=False):
    for card in card_list:
        if card.append:
            return_card(card_list, card, selected_letters, free_spaces, position_list)


def return_card (card_list:list[Box], card, selected_letters:list, free_spaces, position_list:list):

    selected_letters[card.pos] = ""
    position_list.append(card.pos)
    position_list.sort()

    card.pos = free_spaces[len(free_spaces) - 1]
    free_spaces.remove(card.pos)
    
    card.check_append(False)

    card.rectangulo.x, card.rectangulo.y = card_list[card.pos].original_rectangulo.x, 100


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

                if comodin:
                    letter = use_comodin(random_letter, words_founded, word_text)
                    if letter[0] != False:
                        letter_box = Box((x + letter[1],y), (40,100))

                        letter_box.draw_text(surface, letter[0], COLOR_PALABRA, FUENTE_3, font_size=200, shadow=1)

                for word_founded in words_founded:
                    if word_founded == matrix[i][j]:
                        word.draw_text(surface,word_text, COLOR_PALABRA, FUENTE_3, font_size=200, shadow=1)
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
    palabras_secretas = list(lista[0].keys())
    palabra_secretita = random.choice(palabras_secretas)

    combinaciones = lista[0].pop(palabra_secretita)

    return palabra_secretita, combinaciones


def shuffle (card_list, selected_letters, free_spaces, position_list):
    shuffle_card = []
    for card in card_list:
        print(card.letter)
        if card.append is False:
            shuffle_card.append(card.letter)
    for card in card_list:
        if card.append is False:
           
            card.letter = shuffle_card.pop(random.randint(0, len(shuffle_card) - 1))
        print(card.letter)
