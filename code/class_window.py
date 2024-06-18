import pygame

from class_box import Box
class Window:

    def __init__(self, surface, boxes) -> None:
        self.surface = surface
        self.background = None
        self.music = None
        self.box = boxes

        
    def draw_boxes (self, event_l):
        for box in self.box:
            box = Box(box["coords"], box["size"], box["colors"][0], "firebrick1")
            
            box.interactuar(event_l)

            box.draw_box(self.surface, 5)
            box.set_text(self.surface, "Jugar", "green", "System", 50)

       

    def draw_title():
        pass

    def set_bg():
        pass

    def set_music():
        pass


