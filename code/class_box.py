import pygame

#animacion: self.dimensiones | self.posiciones

class Box:
    #CONSTRUCTOR
    def __init__(self, posiciones:tuple, dimensiones:tuple, color_principal:tuple, color_hover:tuple):


        self.posiciones = posiciones
        self.dimensiones = dimensiones
        self.rectangulo = pygame.Rect(posiciones, dimensiones)

        #Color
        self.color_principal = color_principal
        self.color_secundario = (255,255,255)

        #Animación
        self.presionado = False
        self.reduccion = (dimensiones[0] * 0.95, dimensiones[1] * 0.95)

        #Hover
        self.hover = False
        self.color_hover = color_hover

    
    def draw_box (self, ventana, border_radius = -1, border = None, border_width = 0):

        pygame.draw.rect(ventana, self.color_principal, self.rectangulo, border_radius = border_radius)

        if self.hover:
            pygame.draw.rect(ventana, self.color_hover, self.rectangulo, border_radius = border_radius)
        

        if border: 
            pygame.draw.rect(ventana, self.color_secundario, self.rectangulo, width = border_width, border_radius = border_radius)
        

    def set_color (self, first_color:tuple, secondary_color:tuple = None):
        self.color_principal = first_color

        if secondary_color != None:
            self.color_secundario = secondary_color

    def interactuar (self, event) -> bool:
        accion = False
        center = self.rectangulo.center

        if event.type == pygame.MOUSEBUTTONDOWN:  
            if self.rectangulo.collidepoint(event.pos):
                self.presionado = True

                
                self.rectangulo.width = self.reduccion[0]
                self.rectangulo.height = self.reduccion[1]
                self.rectangulo.center = center
                pygame.mixer.music.load(r"code\data\sound\mixkit-arcade-game-jump-coin-216.wav")
                pygame.mixer.music.play(0)
                pygame.mixer.music.set_volume(0.05)

        elif event.type == pygame.MOUSEBUTTONUP:

            self.presionado = False

            self.rectangulo.width = self.dimensiones[0]
            self.rectangulo.height = self.dimensiones[1]
            self.rectangulo.center = center

        elif event.type == pygame.MOUSEMOTION:
            if self.rectangulo.collidepoint(event.pos):
                self.hover = True
            else:
                self.hover = False
        
        return accion

        
    def set_text(self, surface: pygame.Surface , text: str, text_color: str| tuple, font:str, font_size:int):

        x = self.posiciones[0] 
        y = self.posiciones[1] 

        fuente = pygame.font.SysFont(font, font_size)

        text_surface = fuente.render(text, True, text_color)

        #Obtener coordenadas del centro de la caja, y asignarselas al texto en formato rect
        width_center = self.dimensiones[0] / 2
        height_center = self.dimensiones[1] / 2

        text_rect = text_surface.get_rect()
        text_rect.center = (x + width_center, y + height_center)

        surface.blit(text_surface, text_rect)

pygame.init()
clock = pygame.time.Clock()

caja = Box((65,100), (400,200), "deepskyblue3", "deepskyblue4")

ventana = pygame.display.set_mode((800,600))

flag_run = True
while flag_run:
    clock.tick(20)
    #manejador central
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        caja.interactuar (evento)
    
    ventana.fill("black")
            
    caja.draw_box(ventana, border_radius=20, border = True, border_width=6)
    caja.set_color("cadetblue1", secondary_color="deepskyblue3")
    caja.set_text(ventana, "Jugar", "black", "Arial", 20)
    pygame.display.update()

pygame.quit()