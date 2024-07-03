from game_tools.class_image import *

def set_buttons_colors(box_list: list[Box], lista_cfg: list[dict]):
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

def draw_boxes(surface: pygame.Surface, box_list: list[Box], lista_cfg: list[dict]):
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

def draw_boxes_text(surface: pygame.Surface, box_list: list[Box], lista_cfg: list):
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

def draw_images (surface: pygame.Surface, images_list: list[Image]):
    """
    Muestra en pantalla, todos los assets del tipo Image

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        images_list (list[Image]): Lista de assets, con objetos del tipo Image.
    """
    for image in images_list:
        image.draw_image(surface)

def draw_assets(surface: pygame.Surface, box_list: list[Box], images_list: list[Image], list_cfg: list):
    """
    Dibuja todos los assets en pantalla, tanto los interactivos, como
    los estáticos.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        box_list (list[Box]): Lista de assets, con objetos del tipo Box
        images_list (list[Image]): Lista de assets, con objetos del tipo Image.
        list_cfg (list): Lista de assets
    """
    
    draw_images(surface, images_list)
    draw_boxes(surface, box_list, list_cfg)
    draw_boxes_text(surface, box_list, list_cfg)

