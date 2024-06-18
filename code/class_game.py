import pygame
import sys
from class_box import Box
from class_window import Window

boxes_menu = [{"colors": ["gray77", "gray85", "gray85"], "coords": (150,150), "size" : (300,300), "border_width" : 0, "text" : None},
              {"colors": ["gray77", "gray85", "gray85"], "coords": (500,500), "size" : (100,50), "border_width" : 0, "text" : None}]


class Game:

    def __init__(self, size, title, icon:str, box_list:list[dict]) -> None:

        pygame.init()

        self.surface = pygame.display.set_mode((size))
        self.window = Window(self.surface, box_list)

        
        pygame.display.set_caption(title)

        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)

    def run(self):
        event_l = []
        run = True
        
        while run:
            self.surface.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION:
                    event_l.append(event)

            self.window.draw_boxes(event_l)
            
            pygame.display.update()

    def update_window(self):
        self.window(self.surface)



juego = Game((800,600), "a jugar ", r"code\data\img\image.png", boxes_menu)
juego.run()