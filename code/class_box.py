import pygame

#animacion: self.dimensiones | self.posiciones

class Box:
    #CONSTRUCTOR
    def __init__(self, posiciones:tuple, dimensiones:tuple):


        self.posiciones = posiciones
        self.dimensiones = dimensiones
        self.rectangulo = pygame.Rect(posiciones, dimensiones)

        #Color
        self.color_principal = None
        self.color_secundario = (255,255,255)

        #Animación
        self.presionado = False
        self.reduccion = (dimensiones[0] * 0.95, dimensiones[1] * 0.95)

        #Hover
        self.hover = False
        self.color_hover = None

    
    def draw_box (self, ventana, border_radius = -1, border = None, border_width = 0):
        pygame.draw.rect(ventana, self.color_principal, self.rectangulo, border_radius = border_radius)

        if self.hover:
            pygame.draw.rect(ventana, self.color_hover, self.rectangulo, border_radius = border_radius)
        
        if border: 
            pygame.draw.rect(ventana, self.color_secundario, self.rectangulo, width = border_width, border_radius = border_radius)
        

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

        x = self.posiciones[0] 
        y = self.posiciones[1] 

        font_size = font_size * self.rectangulo.width // 300

        fuente = pygame.font.Font(font, font_size)

        text_surface = fuente.render(text, True, text_color)


        #Obtener coordenadas del centro de la caja, y asignarselas al texto en formato rect
        width_center = self.dimensiones[0] / 2
        height_center = self.dimensiones[1] / 2

        text_rect = text_surface.get_rect()
        text_rect.center = (x + width_center, y + height_center)

        surface.blit(text_surface, text_rect)

    def set_image ():
        pass