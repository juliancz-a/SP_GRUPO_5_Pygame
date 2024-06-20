import pygame

#animacion: self.dimensiones | self.posiciones

class Box:
    #CONSTRUCTOR
    def __init__(self, window_size, posiciones:tuple, dimensiones:tuple, press_sound = None, image = None):

        self.window_size = window_size
      
        self.original_posiciones = posiciones
        self.original_dimensiones = dimensiones

        self.posiciones = posiciones
        self.dimensiones = dimensiones
        self.rectangulo = pygame.Rect(self.posiciones, self.dimensiones)

        #Color
        self.color_principal = None
        self.color_secundario = (255,255,255)

        #Animación
        self.presionado = False
        self.reduccion = (dimensiones[0] * 0.95, dimensiones[1] * 0.95)

        #Hover
        self.hover = False
        self.color_hover = None

        #Sonido
        self.sound = press_sound
        #imagen 
        self.image = image
    
    def resize(self, new_window_size):
        # Calcular nueva pos y nuevo tamaño según la división entre la pantalla nueva y la vieja

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
                print("presione el boton")
                self.presionado = True

                if self.sound != None:
                    sound = pygame.mixer.Sound(self.sound)
                    pygame.mixer.Sound.play(sound)
                    pygame.mixer.Sound.set_volume(sound, 0.10)

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
                print("mouse porarriba")
                self.hover = True
            else:
                self.hover = False

        return action
    
    def draw_text(self, surface: pygame.Surface , text: str, text_color: str| tuple, font:str, font_size:int = 20, 
                border = False, shadow = False, border_thickness = 1, border_color = "black"):

        x,y = self.rectangulo.x, self.rectangulo.y

        font_size = font_size * self.rectangulo.width // 300

        fuente = pygame.font.Font(font, font_size)
        text_surface = fuente.render(text, True, text_color)

        #Obtener coordenadas del centro de la caja, y asignarselas al texto en formato rect
        width_center = self.rectangulo.size[0] / 2
        height_center = self.rectangulo.size[1] / 2

        text_rect = text_surface.get_rect()
        text_rect.center = (x + width_center, y + height_center)

        if border:
            for dx in range(-border_thickness, border_thickness + 1):
                for dy in range(-border_thickness, border_thickness + 1):
                    # No renderizar en la posición central (evitar duplicar el texto original)
                    if dx != 0 or dy != 0:
                        offset_rect = text_rect.copy()
                        offset_rect.move_ip(dx, dy)

                        surface.blit(fuente.render(text, True, border_color), offset_rect)
        elif shadow:
            offset_rect = text_rect.copy()
            offset_rect.move_ip(border_thickness, border_thickness)
            surface.blit(fuente.render(text, True, border_color), offset_rect)

        surface.blit(text_surface, text_rect)

    def draw_image (self, surface:pygame.Surface):
        if self.image != None:
            
            image = pygame.image.load(self.image)
            image = pygame.transform.scale(image, self.rectangulo.size)
            
            surface.blit(image, self.rectangulo)

