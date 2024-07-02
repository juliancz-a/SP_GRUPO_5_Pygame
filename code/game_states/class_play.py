import pygame
from constantes import *
from game_tools.class_box import Box
from game_tools.class_image import Image
from game_tools.class_card import *
from game_tools.cards import *

from game_tools.draw_functions import *

from data.config.config import *
from game_tools.words import *
import random



class Play:
    def __init__(self, surface:pygame.Surface, match, datos_palabras, score, comodin, play_assets) -> None:

        self.surface = surface
        self.match = match
        self.initial_time = pygame.time.get_ticks()
        self.music = self.set_music()
        self.volume = True

        #ASSETS
        self.assets_cfg = play_assets
        self.assets = self.init_assets()
    
        self.score = score

        self.background_list = [PLAY_BACKGROUND_1, PLAY_BACKGROUND_2, PLAY_BACKGROUND_3]  

        #CARDS/WORDS SETUP
        self.combinaciones = datos_palabras[1]
        self.letras = datos_palabras[0]
        self.matriz_combinaciones = normalize_words(self.combinaciones)

        self.game_cfg = {"cards_quantity" : 6,
                          "card_list" : set_cards((self.surface.get_width(),100), 6, self.letras),
                          "empty_card_list" : set_cards((self.surface.get_width(), 250), 6),
                          "selected_letters" : ["", "", "", "", "", ""],
                          "founded_words" : [],
                          "pos_libres" : [0,1,2,3,4,5],
                          "pos_ocupadas" : []}

        self.comodin = comodin
        self.random_letter = None
        self.option = None

    def init_assets(self):

        assets = {
                "menu_button" : self.assets_cfg[0]["box"],
                "clear_button" : self.assets_cfg[1]["box"],
                "shuffle_button" : self.assets_cfg[2]["box"],
                "join_button" : self.assets_cfg[3]["box"],
                "timer" : self.assets_cfg[4]["box"],
                "score_text" : self.assets_cfg[5]["box"],
                "comodin_button" : self.assets_cfg[6]["image"],
                "volume_button" : self.assets_cfg[7]["image"],
                "background" : self.assets_cfg[8]["image"]
                }
        
        return assets

    def render(self):
        images_list = [self.assets["background"], self.assets["comodin_button"], self.assets["volume_button"]]
        button_list = [self.assets["menu_button"], self.assets["clear_button"], self.assets["shuffle_button"], self.assets["join_button"]]

        set_buttons_colors(button_list, self.assets_cfg)

        tiempo_transcurrido = (pygame.time.get_ticks() - self.initial_time) // 1000
        tiempo_restante = TIEMPO_LIMITE - tiempo_transcurrido

        if tiempo_restante == 0:
            self.option = 1

        self.surface.fill("black")
       
        draw_assets(self.surface, button_list, images_list, self.assets_cfg)

        draw_cards(self.surface, self.game_cfg["empty_card_list"], transparency=155)
        draw_cards(self.surface, self.game_cfg["card_list"])

        if count_select_letters(self.game_cfg["selected_letters"]) > 2:
            self.assets["join_button"].draw_box(self.surface, 10, 5)
            self.assets["join_button"].draw_text(self.surface, "¡Unir!", "white", FUENTE_1, 60, "shadow", 1, "black", center=True)
        
        self.assets["timer"].draw_text(self.surface, str(tiempo_restante), "white", FUENTE_4, font_size=275, center=True,outline="shadow", outline_thickness=2)
        self.assets["score_text"].draw_text(self.surface, f"Puntaje: {str(self.score)}", "darkslateblue", FUENTE_4, font_size=125, center=True,outline="shadow", outline_thickness=2)

        draw_words(self.surface, self.matriz_combinaciones, self.game_cfg["founded_words"], self.comodin, self.random_letter)

        pygame.display.update()

    def handle_event (self, event):

        score = 0
        volume_img = [{"img" : VOLUME_BUTTON}, {"img" : VOLUME_MUTE_BUTTON}]

        JOIN_CARDS = pygame.USEREVENT + 1
        pygame.time.set_timer(pygame.USEREVENT + 2, 25000)

        if event.type == JOIN_CARDS:
            word = join_cards(self.game_cfg["selected_letters"], self.game_cfg["founded_words"], self.combinaciones)
            if word != False:
                self.game_cfg["founded_words"].append(word)
                reset_pos(self.game_cfg["card_list"], self.game_cfg["selected_letters"], self.game_cfg["pos_ocupadas"], self.game_cfg["pos_libres"])
                self.score += sum_score(score, word)
        
        elif event.type == pygame.USEREVENT + 2:
            self.assets["background"] = Image(select_random_element(self.assets["background"].image_path, self.background_list), (0,0), (1280,720))

        elif count_select_letters(self.game_cfg["selected_letters"]) > 2:
            if self.assets["join_button"].interaction(event):
                pygame.event.post(pygame.event.Event(JOIN_CARDS))
        
        elif self.assets["volume_button"].image_box.interaction(event):
            self.volume = not self.volume
            self.assets["volume_button"] = Image(change_volume(self.volume, volume_img), (10,10), (100,100))

        elif self.assets["menu_button"].interaction(event):
            self.option = 0

        set_cards_interaction(event, self.game_cfg["card_list"], self.game_cfg["selected_letters"], self.game_cfg["pos_libres"], self.game_cfg["pos_ocupadas"])
        if self.comodin == 1:
            action = self.assets["comodin_button"].image_box.interaction(event)
            
            if action:
                self.comodin = 0
                self.random_letter = select_random_letter(self.combinaciones)

        if self.assets["clear_button"].interaction(event):
            reset_pos(self.game_cfg["card_list"], self.game_cfg["selected_letters"], self.game_cfg["pos_ocupadas"], self.game_cfg["pos_libres"])
        
        if self.assets["shuffle_button"].interaction(event):
            shuffle(self.game_cfg["card_list"])

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