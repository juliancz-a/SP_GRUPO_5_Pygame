import pygame
def button_click_event (event:pygame.event, assets_cfg):
    
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


def handle_mouse_event (rectangulo, event) -> dict:
    estado = {
        "presionado" : None,
        "hover" : False,
        "action" : False
    }
    mouse_events = [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]

    for mouse_event in mouse_events:
        if event.type == mouse_event:

            if mouse_event == pygame.MOUSEBUTTONUP:
                estado["presionado"] = False

            if rectangulo.collidepoint(event.pos):
                match mouse_event:
                    case pygame.MOUSEBUTTONDOWN:
                        estado["presionado"] = True

                    case pygame.MOUSEBUTTONUP:
                        estado["action"] = True

                estado["hover"] = True
                    
    return estado

def handle_input_event (write, event, text, max_len):

    if event.type == pygame.KEYDOWN:
        if write:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_ESCAPE:
                text = ""
            elif max_len > len(text) and event.key != pygame.K_RETURN:
                text += event.unicode
    
    return text