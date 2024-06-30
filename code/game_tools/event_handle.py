import pygame
def button_click_event (event, assets_cfg):
    
    selection = None
    button_selected = 0
    
    for asset in assets_cfg:
        if asset["interaction"] == True:
            retorno = asset["box"].interaction(event)

            if retorno:
                selection = button_selected
                break

            button_selected += 1
    
    return selection


def handle_mouse_event (rectangulo, event):
    estado = False
    mouse_events = [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]

    for mouse_event in mouse_events:
        if event.type == mouse_event:
            if rectangulo.collidepoint(event.pos):
                estado = True

    return estado
