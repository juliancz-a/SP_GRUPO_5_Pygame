import pygame

def handle_mouse_event (rectangulo: pygame.Rect, event: pygame.event.Event) -> dict:
    """Gestión de eventos de los botones de la clase Box.

    Args:
        rectangulo (pygame.Rect): Botón
        event (pygame.event.Event): Evento capturado

    Returns:
        dict: Diccionario con todos los estados activos del botón al momento."""
    
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

def handle_input_event(input_box_state: bool, event: pygame.event.Event, text: str,
                       max_len: int) -> str:
    """
    Gestiona los eventos de entrada para el nickname del usuario.

    Args:
        write (bool): Estado de la caja de texto.
        event (pygame.event): Evento de capturado.
        text (str): Texto en blanco donde se coloca el nickname del usuario.
        max_len (int): Máximo de caracteres permitidos.

    Returns:
        str: Devuelve el nickname ingresado por el usuario.
    """

    if event.type == pygame.KEYDOWN:
        if input_box_state:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_ESCAPE:
                text = ""
            elif max_len > len(text) and event.key != pygame.K_RETURN:
                text += event.unicode

    return text

def get_option_selected (event: pygame.event.Event, assets_cfg: list) -> int:
    """Obtener una opción para modificar la escena a partir de la interacción
    con un botón.

    Args:
        event (pygame.event.Event): Evento de capturado
        assets_cfg (list): Listado de recursos de una escena en particular

    Returns:
        int: Opción solicitada
    """
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

