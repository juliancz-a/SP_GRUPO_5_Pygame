import pygame
from game_tools.event_handle import *
#animacion: self.dimensiones | self.posiciones

class Box:
    #CONSTRUCTOR
    def __init__(self, posiciones:tuple, dimensiones:tuple, press_sound = None):

        self.posiciones = posiciones
        self.dimensiones = dimensiones
        self.rectangulo = pygame.Rect(self.posiciones, self.dimensiones)
        self.original_rectangulo = pygame.Rect(self.posiciones, self.dimensiones)

        #Color
        self.color_principal = None
        self.color_secundario = None
        self.color_hover = None

        #Animación
        self.presionado = False
        self.reduccion = (dimensiones[0] * 0.95, dimensiones[1] * 0.95)

        #Hover
        self.hover = False
        
        #Sonido
        self.sound = press_sound

        self.activo = False

    def draw_box (self, surface, border_radius = -1, border_width = 0):

        pygame.draw.rect(surface, self.color_principal, self.rectangulo, border_radius = border_radius)

        if self.hover:
            pygame.draw.rect(surface, self.color_hover, self.rectangulo, border_radius = border_radius)
        
        if border_width > 0: 
            pygame.draw.rect(surface, self.color_secundario, self.rectangulo, width = border_width, border_radius = border_radius)
        

    def set_color (self, first_color:tuple, secondary_color:tuple, hover_color:tuple):
        
        self.color_principal = first_color

        self.color_secundario = secondary_color

        self.color_hover = hover_color

    def interaction (self, event) -> bool:
        action = False

        center = self.rectangulo.center

        estado = handle_mouse_event(self.rectangulo, event)
        
        if estado["presionado"] == True:
            if self.sound != None:
                sound = pygame.mixer.Sound(self.sound)
                pygame.mixer.Sound.play(sound)
                pygame.mixer.Sound.set_volume(sound, 0.10)

            self.rectangulo.size = (self.reduccion[0], self.reduccion[1])
            self.rectangulo.center = center
        
        elif estado["presionado"] == False:
            if estado["action"]:
                action = True

            self.rectangulo.size = (self.dimensiones[0], self.dimensiones[1])
            self.rectangulo.center = center

        if estado["hover"] == True:
            self.hover = True
        else:
            self.hover = False

        return action
    
    def draw_text(self, surface: pygame.Surface , text: str, text_color: str| tuple, font:str, font_size:int = 20, 
                outline = None, outline_thickness = 1, outline_color = "black",  center = False):

        x,y = self.rectangulo.x, self.rectangulo.y

        font_size = font_size * self.rectangulo.width // 300

        fuente = pygame.font.Font(font, font_size)
        text_surface = fuente.render(text, True, text_color)

        #Obtener coordenadas del centro de la caja, y asignarselas al texto en formato rect
        width_center = self.rectangulo.size[0] / 2
        height_center = self.rectangulo.size[1] / 2

        text_rect = text_surface.get_rect()
        
        if center:
            text_rect.center = (x + width_center, y + height_center - 3)
        else:
            text_rect.topleft = x,y
    

        match outline:
            case "border":
                for dx in range(-outline_thickness, outline_thickness + 1):
                    for dy in range(-outline_thickness, outline_thickness + 1):
                        # No renderizar en la posición central (evitar duplicar el texto original)
                        if dx != 0 or dy != 0:
                            offset_rect = text_rect.copy()
                            offset_rect.move_ip(dx, dy)

                            surface.blit(fuente.render(text, True, outline_color), offset_rect)
            case "shadow":
                offset_rect = text_rect.copy()
                offset_rect.move_ip(outline_thickness, outline_thickness)
                surface.blit(fuente.render(text, True, outline_color), offset_rect)

        surface.blit(text_surface, text_rect)
