import pygame
from game_tools.event_handle import *
from game_tools.draw_functions import *
#animacion: self.dimensiones | self.posiciones

class Box:
    #CONSTRUCTOR
    def __init__(self, posiciones:tuple, dimensiones:tuple, press_sound = None):
        """Creación de objeto tipo Box (caja) para su renderización e interacción.

        Args:
            posiciones (tuple): Posiciones del objeto, deben estar dentro de una superficie
            dimensiones (tuple): Dimensiones del objeto.
            press_sound (_type_, optional): Sonido del objeto al ser presionado.
        """
        self.posiciones = posiciones
        self.dimensiones = dimensiones
        self.rectangulo = pygame.Rect(self.posiciones, self.dimensiones)
        self.original_rectangulo = pygame.Rect(self.posiciones, self.dimensiones)

        #Color
        self.color_principal = None
        self.color_secundario = None
        self.color_hover = None

        #Animación
        self.reduccion = (dimensiones[0] * 0.95, dimensiones[1] * 0.95)

        #Hover
        self.hover = False
        
        #Sonido
        self.sound = press_sound

    def draw_box (self, surface:pygame.Surface, border_radius:int = -1, 
                  border_width:int = 0):
        """Dibujar en pantalla el rectangulo lógico creado.

        Args:
            surface (pygame.Surface): Superficie sobre la cual dibujar el rectangulo
            border_radius (int, optional): Radio de redondeo del rectángulo
            border_width (int, optional): Longitud del borde del rectángulo"""

        pygame.draw.rect(surface, self.color_principal, self.rectangulo,
                        border_radius = border_radius)

        if self.hover:
            pygame.draw.rect(surface, self.color_hover, self.rectangulo, 
                            border_radius = border_radius)
        
        if border_width > 0: 
            pygame.draw.rect(surface, self.color_secundario, self.rectangulo, 
                            width = border_width, border_radius = border_radius)
        

    def set_color (self, first_color:tuple, secondary_color:tuple, hover_color:tuple):
        """Inicializar los colores de un rectángulo físico

        Args:
            first_color (tuple): Color principal
            secondary_color (tuple): Color secundario (borde)
            hover_color (tuple): Color de hover (puntero sobre el rectángulo)"""
        self.color_principal = first_color

        self.color_secundario = secondary_color

        self.color_hover = hover_color

    def interaction (self, event:pygame.event.Event) -> bool:
        """Registrar la interacción del usuario con el rectángulo (bóton), 
        según el evento capturado.

        Args:
            event (pygame.event.Event): Evento capturado

        Returns:
            bool: False [No se ha presionado el botón] 
            True [Se ha presionado con el botón]
        """
        
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
    
    def draw_text(self, surface: pygame.Surface , text: str, text_color: str| tuple, 
                  font:str, font_size:int = 20, outline:bool = None,
                  outline_thickness:int = 1, outline_color:str = "black", center:int = False):
        """Dibujar texto sobre el rectángulo. El rectangúlo puede estar dibujado o no.

        Args:
            surface (pygame.Surface): Superficie sobre la cual dibujar el texto.
            text (str): Texto determinado a dibujar
            text_color (str | tuple): Color de texto
            font (str): Fuente de texto
            font_size (int, optional): Tamaño de fuente.
            outline (bool, optional): Utilizar contorno para el texto.
            outline_thickness (int, optional): Espesor del contorno
            outline_color (str, optional): Color del contorno
            center (bool, optional): Utilizar un texto centrado en el rectángulo"""
        
        font_size = font_size * self.rectangulo.width // 300

        fuente = pygame.font.Font(font, font_size)
        text_surface = fuente.render(text, True, text_color)

        width_center = self.rectangulo.size[0] / 2
        height_center = self.rectangulo.size[1] / 2

        text_rect = text_surface.get_rect()
        
        if center:
            text_rect.center = (self.rectangulo.x + width_center, 
                                self.rectangulo.y + height_center - 3)
        else:
            text_rect.topleft = (self.rectangulo.x, self.rectangulo.y)
    
        match outline:
            case "border":
                draw_text_outline(surface, fuente, text, text_rect, outline_thickness, outline_color)
            case "shadow":
                draw_text_shadow(surface, fuente, text, text_rect, outline_thickness, outline_color)

        surface.blit(text_surface, text_rect)