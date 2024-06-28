from class_box import Box
from class_image import *

def set_buttons_colors(button_list, list_cfg):
        for i in range(len(button_list)):
            button_list[i].set_color(*list_cfg[i]["colors"])

def draw_buttons(surface, button_list:list[Box], lista_cfg):
    for i in range(len(button_list)):
        button_list[i].draw_box(surface, *lista_cfg[i]["config"])

def draw_buttons_text(surface, button_list, lista_cfg):
    for i in range(len(button_list)):
        button_list[i].draw_text(surface, *lista_cfg[i]["text"])

def draw_images (surface, images_list:list[Image]):
    for image in images_list:
        image.draw_image(surface)

def draw_assets(surface, button_list, images_list, list_cfg):
    
    draw_images(surface, images_list)
    draw_buttons(surface, button_list, list_cfg)
    draw_buttons_text(surface, button_list, list_cfg)

