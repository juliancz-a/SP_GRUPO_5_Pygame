import pygame
from constantes import *
from game_tools.class_box import Box
from game_tools.class_image import Image
from game_tools.card import *

from game_tools.draw_functions import *

from data.config.config import *
from game_tools.words import *
import random



class Play:
    def __init__(self, surface:pygame.Surface, match, lista, score, comodin, play_assets) -> None:

        self.surface = surface
        self.match = match
        self.play_assets = play_assets
        #BOTONES
        self.comodin_button = Image(COMODIN, (1070, 220), (100,100), image_hover_path=COMODIN_HOVER,  press_sound=PRESS_COMODIN_SOUND)

        self.join_button = Box((770,400), (120,70))
        self.menu_button = self.play_assets[0]["box"]
        self.clear_button = self.play_assets[1]["box"]
        self.shuffle_button = self.play_assets[2]["box"]

        self.box_list = [self.play_assets[0]["box"], self.play_assets[1]["box"], self.play_assets[2]["box"]]
        
        #TEXTO
        self.timer = Box((618, 420), (50,50)) 
        self.initial_time = pygame.time.get_ticks()

        self.score = score
        self.score_text = Box((400, 410), (100,50))
    
        self.music = self.set_music()
        #IMG
        self.background = Image(PLAY_BACKGROUND_1, (0,0), (1280,720))
        self.background_list = [PLAY_BACKGROUND_1, PLAY_BACKGROUND_2, PLAY_BACKGROUND_3]  

        self.images = [self.background, self.comodin_button]

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
    
        set_buttons_colors(self.box_list, self.play_assets)
        self.join_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")

        tiempo_transcurrido = (pygame.time.get_ticks() - self.initial_time) // 1000
        tiempo_restante = TIEMPO_LIMITE - tiempo_transcurrido

        if tiempo_restante == 0:
            self.option = 1

        self.surface.fill("black")
       
        draw_assets(self.surface, self.box_list, [self.background, self.comodin_button], self.play_assets)

        draw_cards(self.surface, self.cards_cfg["empty_card_list"], transparency=155)
        draw_cards(self.surface, self.cards_cfg["card_list"])

        if count_select_letters(self.cards_cfg["selected_letters"]) > 2:
            self.join_button.draw_box(self.surface, 10, 5)
            self.join_button.draw_text(self.surface, "¡Unir!", "white", FUENTE_1, 60, "shadow", 1, "black", center=True)
        
        self.timer.draw_text(self.surface, str(tiempo_restante), "white", FUENTE_4, font_size=275, center=True,outline="shadow", outline_thickness=2)
        self.score_text.draw_text(self.surface, f"Puntaje: {str(self.score)}", "darkslateblue", FUENTE_4, font_size=125, center=True,outline="shadow", outline_thickness=2)

        draw_words(self.surface, self.matriz_combinaciones, self.cards_cfg["founded_words"], self.comodin, self.random_letter)

        pygame.display.update()

    def handle_event (self, event):

        score = 0
        join = False
        menu = False

        JOIN_CARDS = pygame.USEREVENT + 1
        pygame.time.set_timer(pygame.USEREVENT + 2, 25000)

        if event.type == JOIN_CARDS:
            word = join_cards(self.cards_cfg["selected_letters"], self.cards_cfg["founded_words"], self.combinaciones)
            if word != False:
                self.cards_cfg["founded_words"].append(word)
                reset_pos(self.cards_cfg["card_list"], self.cards_cfg["selected_letters"], self.cards_cfg["pos_ocupadas"], self.cards_cfg["pos_libres"])
                self.score += sum_score(score, word)
        
        elif event.type == pygame.USEREVENT + 2:
            self.background = Image(select_random_element(self.background.image_path, self.background_list), (0,0), (1280,720))

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

        pygame.mixer.music.load(PLAY_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
    
    def update_play_instance (self):
        self.match += 1
        
        data = self.match, self.score

        return data