import pygame

def set_buttons_colors(box_list: list, lista_cfg: list[dict]) -> None:
    """
    Asigna los colores del botón, si es que fueron asignados.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        box_list (list[Box]): Lista de assets, con objetos del tipo Box
        lista_cfg (list): Lista de assets
    """
    for i in range(len(box_list)):
        if len(lista_cfg[i]["colors"]) > 0:
            box_list[i].set_color(*lista_cfg[i]["colors"])

def draw_boxes(surface: pygame.Surface, box_list: list, 
               lista_cfg: list[dict]) -> None:
    """
    Dibuja el botón que se encuentra en el asset cargado de la lista, si
    es que lo tiene asignado.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        box_list (list[Box]): Lista de assets, con objetos del tipo Box
        lista_cfg (list): Lista de assets
    """
    for i in range(len(box_list)):
        if len(lista_cfg[i]["config"]) > 0:
            box_list[i].draw_box(surface, *lista_cfg[i]["config"])

def draw_boxes_text(surface: pygame.Surface, box_list: list,
                    lista_cfg: list) -> None:
    """
    Dibuja el texto que se encuentra en el asset cargado de la lista, si
    es que tiene uno asignado.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        box_list (list[Box]): Lista de assets, con objetos del tipo Box
        lista_cfg (list): Lista de assets
    """
    for i in range(len(box_list)):
        if len(lista_cfg[i]["text"]) > 0:
            box_list[i].draw_text(surface, *lista_cfg[i]["text"])

def draw_images (surface: pygame.Surface, images_list: list) -> None:
    """
    Muestra en pantalla, todos los assets del tipo Image

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        images_list (list): Lista de assets, con objetos del tipo Image.
    """
    for image in images_list:
        image.draw_image(surface)

def draw_assets(surface: pygame.Surface, box_list: list,
                images_list: list, list_cfg: list) -> None:
    """
    Dibuja todos los assets en pantalla, tanto los interactivos, como
    los estáticos.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        list (list[Box]): Lista de assets, con objetos del tipo Box
        images_list (list): Lista de assets, con objetos del tipo Image.
        list_cfg (list): Lista de assets
    """
    
    draw_images(surface, images_list)
    draw_boxes(surface, box_list, list_cfg)
    draw_boxes_text(surface, box_list, list_cfg)

def draw_text_outline(surface: pygame.Surface, font: pygame.font,
                        text: str, text_rect: pygame.Rect, outline_thickness: int,
                        outline_color: tuple) -> None:
    """Dibuja un contorno alrededor de las letras.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        font (pygame.font): Fuente utilizada para las letras.
        text (str): Texto deseado para el contorno.
        text_rect (pygame.Rect): Rect donde se encuentra la letra original.
        outline_thickness (int): Grosor del contorno.
        outline_color (tuple): Color del contorno.
    """
    
    for dx in range(-outline_thickness, outline_thickness + 1):
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:
                offset_rect = text_rect.copy()
                offset_rect.move_ip(dx, dy)
                surface.blit(font.render(text, True, outline_color), offset_rect)

def draw_text_shadow(surface: pygame.Surface, font: pygame.font, text: str,
                    text_rect: pygame.Rect, outline_thickness: int,
                    outline_color: tuple) -> None:
    """
    Dibuja una sombra alrededor de las letras.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        font (pygame.font): Fuente utilizada para las letras.
        text (str): Texto deseado para el contorno.
        text_rect (pygame.Rect): Rect donde se encuentra la letra original.
        outline_thickness (int): Pixeles de diferencia entre la letra y la sombra.
        outline_color (tuple): Color del sombreado.
    """
    offset_rect = text_rect.copy()
    offset_rect.move_ip(outline_thickness, outline_thickness)
    surface.blit(font.render(text, True, outline_color), offset_rect)
