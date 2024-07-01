import pygame
from game_tools.class_image import *
from data.config.assets_cfg import *
from game_tools.draw_functions import *
from game_tools.event_handle import *
from game_tools.extra_functions import *

class Help:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.menu_button = HELP_ASSETS[0]["box"]

        self.background = Image(HELP_BACKGROUND, (0,0), (1280,720))

        self.comodin_button_img = Image (COMODIN, (580, 505), (100, 100))
        self.shuffle_button_img = Image (r"code\data\img\shuffle_button.png", (400, 500), (160, 100))
        self.clear_button_img = Image (r"code\data\img\clear_button.png", (690, 500), (160, 100))

        self.config_list = HELP_ASSETS
        self.box_list  = [self.menu_button]
        self.image_list = [self.background, self.comodin_button_img, self.clear_button_img, self.shuffle_button_img]

        self.option = None

    def render(self):

        set_buttons_colors(self.box_list, self.config_list)

        self.surface.fill("aquamarine4")
        
        draw_assets(self.surface, self.box_list, self.image_list, self.config_list)

        render_multi_line(self.surface, HELP_TEXT, 620, 10, 150, center_text= True)

        pygame.display.update()

    def handle_event (self, event):
        self.option = button_click_event(event, self.config_list)

    def update(self):
        selection = None

        match self.option:
            case 0:
                selection = "menu"
        
        return selection
    