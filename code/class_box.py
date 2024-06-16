import pygame
class Box:
    #CONSTRUCTOR
    def __init__(self, dimensiones:tuple, pos:tuple) -> pygame.Rect:
        self.color_principal = (255,255,255)
        self.color_secundario = (255,255,255)
        self.color_click = (255,255,255)
        self.dimensiones = (None,None)
        self.posicion = (None,None)
        self.texto = None

    def render_box (self):
        pass

    def set_color (first_color:tuple, secondary_color:tuple = None, color_on_click:tuple = None):
        pass

    def presionar (self, mouse_pos:tuple):
        pass

    def set_text ():
        pass

    def set_animation ():

