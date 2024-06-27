import pygame
from class_box import Box
from constantes import  *

class Image:
    def __init__(self, image_path, coords, dimensiones, image_hover_path = None, press_sound = None) -> None:

        self.image_surface = pygame.image.load(image_path)
        self.image_surface = pygame.transform.scale(self.image_surface, dimensiones)

       
        self.image_hover = image_hover_path

        self.image_box = Box(coords, dimensiones, press_sound = press_sound)
    
    def draw_image (self, surface:pygame.Surface, transparency:int = None):
        if transparency != None:

            image = image.convert_alpha()
            image.set_alpha(transparency)

            pygame.draw.rect(surface, (128,128,128,50), self.image_box.rectangulo, border_radius=10)

        surface.blit(self.image_surface, self.image_box.rectangulo)

        if self.image_hover != None:
            self.image_hover = pygame.image.load(self.image_hover)
            self.image_hover = pygame.transform.scale(self.image_hover, self.image_box.rectangulo)
            surface.blit(self.image_hover, self.image_box.rectangulo)