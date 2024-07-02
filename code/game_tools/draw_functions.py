from game_tools.class_box import Box
from game_tools.class_image import *

def set_buttons_colors(button_list, lista_cfg):
        for i in range(len(button_list)):
            if len(lista_cfg[i]["colors"]) > 0:
                button_list[i].set_color(*lista_cfg[i]["colors"])

def draw_boxes(surface, button_list:list[Box], lista_cfg):
    for i in range(len(button_list)):
        if len(lista_cfg[i]["config"]) > 0:
            button_list[i].draw_box(surface, *lista_cfg[i]["config"])

def draw_boxes_text(surface, button_list, lista_cfg):
    for i in range(len(button_list)):
        if len(lista_cfg[i]["text"]) > 0:
            button_list[i].draw_text(surface, *lista_cfg[i]["text"])

def draw_images (surface, images_list:list[Image]):
    for image in images_list:
        image.draw_image(surface)

def draw_assets(surface, button_list, images_list, list_cfg, conditionals = False):
    
    draw_images(surface, images_list)
    draw_boxes(surface, button_list, list_cfg)
    draw_boxes_text(surface, button_list, list_cfg)

