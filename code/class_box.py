import pygame
class Box:
    #CONSTRUCTOR
    def __init__(self, dimensiones:tuple, pos:tuple) -> pygame.Rect:
        self.color_principal = (255,255,255)
        self.color_secundario = (255,255,255)
        self.color_click = (255,255,255)
        self.dimensiones = dimensiones
        self.posicion = pos
        self.texto = None

    def render_box (self, ventana):
        pygame.draw.rect(ventana, self.color_principal, (self.posicion, self.dimensiones))

    def set_color (self, first_color:tuple, secondary_color:tuple = None, color_on_click:tuple = None):
        self.color_principal = first_color

        if secondary_color:
            self.color_secundario = secondary_color
        
        if color_on_click:
            self.color_click = color_on_click

    def presionar (self, mouse_pos:tuple):
        pass

    def set_text(self, text: str):
        self.texto = text

    def set_animation ():
        pass

