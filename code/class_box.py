import pygame

#animacion: self.dimensiones | self.posiciones

class Box:
    #CONSTRUCTOR
    def __init__(self, window_size, posiciones:tuple, dimensiones:tuple):
        self.original_posiciones = posiciones
        self.original_dimensiones = dimensiones

        self.posiciones = posiciones
        self.dimensiones = dimensiones
        self.rectangulo = pygame.Rect(self.posiciones, self.dimensiones)

        self.window_size = window_size

        #Color
        self.color_principal = None
        self.color_secundario = (255,255,255)

        #Animación
        self.presionado = False
        self.reduccion = (dimensiones[0] * 0.95, dimensiones[1] * 0.95)

        #Hover
        self.hover = False
        self.color_hover = None

    
    def resize(self, new_window_size):
        # Calculate the new position and dimensions based on the new window size
        self.posiciones = (
            int(self.original_posiciones[0] * new_window_size[0] / self.window_size[0]),
            int(self.original_posiciones[1] * new_window_size[1] / self.window_size[1])
        )
        self.dimensiones = (
            int(self.original_dimensiones[0] * new_window_size[0] / self.window_size[0]),
            int(self.original_dimensiones[1] * new_window_size[1] / self.window_size[1])
        )
        self.rectangulo = pygame.Rect(self.posiciones, self.dimensiones)
        self.reduccion = (self.dimensiones[0] * 0.95, self.dimensiones[1] * 0.95)

    
    def draw_box (self, surface, border_radius = -1, border = None, border_width = 0):


        pygame.draw.rect(surface, self.color_principal, self.rectangulo, border_radius = border_radius)

        if self.hover:
            pygame.draw.rect(surface, self.color_hover, self.rectangulo, border_radius = border_radius)
        
        if border: 
            pygame.draw.rect(surface, self.color_secundario, self.rectangulo, width = border_width, border_radius = border_radius)
        

    def set_color (self, first_color:tuple, secondary_color:tuple, hover_color:tuple):
        self.color_principal = first_color

        self.color_secundario = secondary_color

        self.color_hover = hover_color

    def interaction (self, event) -> bool:
        action = False

        center = self.rectangulo.center
       
        if event.type == pygame.MOUSEBUTTONDOWN:  

            if self.rectangulo.collidepoint(event.pos):

                self.presionado = True

                pygame.mixer.music.load(r"code\data\sound\mixkit-arcade-game-jump-coin-216.wav")
                pygame.mixer.music.play(0)
                pygame.mixer.music.set_volume(0.05)

                self.rectangulo.width = self.reduccion[0]
                self.rectangulo.height = self.reduccion[1]
                self.rectangulo.center = center

        elif event.type == pygame.MOUSEBUTTONUP:

            if self.rectangulo.collidepoint(event.pos):
                self.presionado = False

                self.rectangulo.width = self.dimensiones[0]
                self.rectangulo.height = self.dimensiones[1]
                self.rectangulo.center = center
                action = True

            else: 
                self.rectangulo.width = self.dimensiones[0]
                self.rectangulo.height = self.dimensiones[1]
                self.rectangulo.center = center

        elif event.type == pygame.MOUSEMOTION:
            
            if self.rectangulo.collidepoint(event.pos):
                self.hover = True
            else:
                self.hover = False

        return action
        
    def draw_text(self, surface: pygame.Surface , text: str, text_color: str| tuple, font:str, font_size:int = 20):

        x,y = self.rectangulo.x, self.rectangulo.y

        font_size = font_size * self.rectangulo.width // 300

        fuente = pygame.font.Font(font, font_size)

        text_surface = fuente.render(text, True, text_color)

        border_thickness = 1
        border_color = "gray0"

        #Obtener coordenadas del centro de la caja, y asignarselas al texto en formato rect
        width_center = self.dimensiones[0] / 2
        height_center = self.dimensiones[1] / 2

        text_rect = text_surface.get_rect()
        text_rect.center = (x + width_center, y + height_center)

        for dx in range(-border_thickness, border_thickness + 1):
            for dy in range(-border_thickness, border_thickness + 1):
                # No renderizar en la posición central (evitar duplicar el texto original)
                if dx != 0 or dy != 0:
                    offset_rect = text_rect.copy()
                    offset_rect.move_ip(dx, dy)
                    surface.blit(fuente.render(text, True, border_color), offset_rect)

        surface.blit(text_surface, text_rect)

    def set_image ():
        pass