import pygame
from class_box import Box
from constantes import  *

class Image:
    def __init__(self, image_path, coords, dimensiones, image_hover_path = None, press_sound = None) -> None:

        self.image_box = Box(coords, dimensiones, press_sound = press_sound)
        
        self.image_surface = pygame.image.load(image_path)
        self.image_surface = pygame.transform.scale(self.image_surface, dimensiones)

        self.image_hover = None
        if image_hover_path != None:
            self.image_hover = pygame.image.load(image_hover_path)
            self.image_hover = pygame.transform.scale(self.image_hover, self.image_box.rectangulo.size)

    
    def draw_image (self, surface:pygame.Surface, transparency:int = 255):
        image_alpha = self.image_surface.convert_alpha()
        image_alpha.set_alpha(transparency)

        surface.blit(image_alpha, self.image_box.rectangulo)
        if self.image_hover != None and self.image_box.hover:
            surface.blit(self.image_hover, self.image_box.rectangulo)