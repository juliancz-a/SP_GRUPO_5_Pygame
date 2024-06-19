import pygame

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.container = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

    def render(self, screen):
        pygame.draw.rect(screen, "darkgray", self.container)
        pygame.draw.rect(screen, "indigo", self.button_rect, 4)

    def move_slider(self, mouse_pos):
        self.button_rect.centerx = mouse_pos[0]

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return ((button_val / val_range) * (self.max - self.min) + self.min) * 0.01


pygame.init()

ventana = pygame.display.set_mode((800,600))

slider = Slider((200, 230), (200, 40), 0.2, 0, 100)
volume = 0.10

flag_run = True
while flag_run:
    #manejador central
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load(r"code\sounds\click.wav")
            pygame.mixer.music.play(0)
            pygame.mixer.music.set_volume(volume)
            

    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    if slider.container.collidepoint(mouse_pos) and mouse[0]:
        slider.move_slider(mouse_pos)
    volume = slider.get_value()

    ventana.fill("black")
    slider.render(ventana)
            
    pygame.display.update()


pygame.quit()