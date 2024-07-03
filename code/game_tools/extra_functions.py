from game_tools.class_box import *
from constantes import *
import random

def ordenar_elementos (list: list[dict], orden: int, key: str = None) -> str:
    """
    Método de ordenamiento bubble sort.

    Args:
        list (list[dict]): Lista a ordenar
        orden (int): Tipo de orden (Ascendente o descendente)
        key (str, optional): En caso de existir, se ordena la lista según
        el valor de la key.

    Returns:
        str: El primer elemento de la lista.
    """

    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
                
            match orden:
                case 1:
                    if key != None:
                        print(list[i][key], list[j][key])
                        if list[i][key] >= list[j][key]:
                            swap(list, i, j)

                    else:
                        if list[i] >= list[j]:
                            swap(list, i, j)
                case 2:
                    if key != None:
                        if list[i][key] <= list[j][key]:
                            swap(list, i, j)
                    else:   
                        if list[i] <= list[j]:
                            swap(list, i, j)
    
    first_element = list[0]

    return first_element

def swap(list:list[dict], a:int, b:int):
    """
    Intercambia los elementos de la lista en posiciones 'a' y 'b'.

    Args:
        list (list[dict]): Lista donde se encuentran los elementos.
        a (int): Primer elemento a intercambiar.
        b (int): Segundo elemento a intercambiar.
    """
    aux = list[a]
    list[a] = list[b]
    list[b] = aux

def operacion(x, y, operacion):
    return operacion(x, y)


def render_multi_line(surface: pygame.Surface, text: str, x: int, y: int, font_size: int, center_text: bool = False):
    """
    Separa un texto según los saltos de línea, para mostrar línea por línea en pantalla.

    Args:
        surface (pygame.Surface): Superficie de la aplicación.
        text (str): Oración a mostrar en pantalla.
        x (int): Coordenada horizontal en la superficie.
        y (int): Coordenada vertical en la superficie.
        font_size (int): Tamaño de las letras a mostrar en pantalla.
        center_text (bool, optional): Inicializda en False. Si es True, escribe el texto.
        desde el punto central de la pantalla.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        box_line = Box((x, y + font_size // 3 * i), (50,50))
        box_line.draw_text(surface, line, "white", FUENTE_1, font_size, "shadow", 2, "black", center = center_text)

def select_random_element(actual_element: str | int, lista_elementos: list) -> str | int:
    """
    Elige un elemento aleatorio de una lista

    Args:
        actual_element (str | int): Elemento actualmente seleccionado.
        lista_elementos (list): La lista con todos los elementos a usar.

    Returns:
        str | int: Devuelve el elemento seleccionado aleatoriamente.
    """
    
    random_element = random.choice(lista_elementos)
    while random_element == actual_element:
        random_element = random.choice(lista_elementos)

    return random_element

def change_volume (volume, volume_img)  -> bool:
    match volume:
        case True:            
            volume_img = (volume_img[0]["img"])
        case False:        
            volume_img = (volume_img[1]["img"])
    
    return volume_img