import pygame
from class_window import Window
from class_box import Box
class Game:

    def __init__(self, size, title, icon) -> None:
        self.window = Window(size, title, icon)
        self.running = None
        self.clock = None

    def run(self):

        
        self.running = True

        pygame.init()

        self.window.render_window()

        self.clock = pygame.time.Clock()
        self.clock.tick(15)

        while self.running:
            print("JUGAR!")


    def quit(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.quit()

    def get_box (posiciones:tuple, dimensiones:tuple, color_principal:tuple, color_hover):
        box = Box(posiciones, dimensiones, color_principal, color_hover)
        return box











juego = Game((800,600), "a jugar ", r"code\data\img\image.png")

juego.run()

juego.quit()