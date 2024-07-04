import pygame
from game_tools.class_box import Box
from constantes import  *

class Image:
    def __init__(self, image_path: str, coords: tuple, dimensiones: tuple, 
                image_hover_path: str = None, press_sound: str = None) -> None:
        """Creacion de un objeto tipo Image (imagen), para su renderización e 
        interacción. Comparte propiedades de un objeto del tipo Box.

        Args:
            image_path (str): Ruta de la imagen del objeto
            coords (tuple): Coordenadas del objeto, deben estar dentro de una superficie
            dimensiones (tuple): Dimensiones del objeto
            image_hover_path (str, optional): Ruta de la imagen hover del objeto
            press_sound (str, optional): Ruta del sonido del objeto al presionarlo
        """

        self.image_box = Box(coords, dimensiones, press_sound = press_sound)
        self.image_path = image_path
        
        self.image_surface = pygame.image.load(self.image_path)
        self.image_surface = pygame.transform.scale(self.image_surface, dimensiones)

        self.image_hover = None
        if image_hover_path != None:
            self.image_hover = pygame.image.load(image_hover_path)
            self.image_hover = pygame.transform.scale(self.image_hover, 
                                                      self.image_box.rectangulo.size)

    
    def draw_image (self, surface: pygame.Surface, transparency: int = 255) -> None:
        """Dibujar una imagen sobre una superficie.

        Args:
            surface (pygame.Surface): Superficie sobre la cual dibujar la imagen
            transparency (int, optional): Transparencia de la imagen
        """
        image_alpha = self.image_surface.convert_alpha()
        image_alpha.set_alpha(transparency)

        surface.blit(image_alpha, self.image_box.rectangulo)
        
        if self.image_hover != None and self.image_box.hover:
            surface.blit(self.image_hover, self.image_box.rectangulo)