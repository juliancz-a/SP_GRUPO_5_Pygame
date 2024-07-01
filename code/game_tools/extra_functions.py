from game_tools.class_box import *
from constantes import *

def ordenar_elementos (list:list[dict], orden:int, key = None):

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
    return list[0]

def swap(list:list[dict], a:int, b:int):
    aux = list[a]
    list[a] = list[b]
    list[b] = aux

def operacion(x, y, operacion):
    return operacion(x, y)


def render_multi_line(surface, text, x, y, font_size, center_text = False):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        box_line = Box((x, y + font_size // 3 * i), (50,50))
        box_line.draw_text(surface, line, "white", FUENTE_1, font_size, "shadow", 2, "black", center = center_text)