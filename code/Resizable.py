import pygame, sys

pygame.init()
# Create the window, saving it to a variable.
surface = pygame.display.set_mode((350, 250), pygame.RESIZABLE)
pygame.display.set_caption("Example resizable window")

while True:
    surface.fill((255,255,255))

    # Draw a red rectangle that resizes with the window.
    pygame.draw.rect(surface, (200,0,0), (surface.get_width()/3,
      surface.get_height()/3, surface.get_width()/3,
      surface.get_height()/3))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
            

pygame.init()

clock = pygame.time.Clock()
correctas = []
tiempo_inicial = pygame.time.get_ticks()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

run = True
while run:
    clock.tick(30)
    
    ventana.fill(BLANCO)

    lista_eventos = pygame.event.get() 
    for evento in lista_eventos: 
        if evento.type == pygame.QUIT:
            run = False


    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_transcurrido *= 0.001
    print(f"{(tiempo_transcurrido):.02f}")

    if tiempo_transcurrido >= TIEMPO_LIMITE:
        print("a")
        run = False
                
    pygame.display.update()

pygame.quit()