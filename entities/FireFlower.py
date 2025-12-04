import pygame
from entities.EntityBase import EntityBase
from classes.Sprites import Sprites

spriteCollection = Sprites().spriteCollection

class FireFlower(EntityBase):
    def __init__(self, x, y):
        super().__init__(x, y, gravity=0)  # tidak jatuh
        self.type = "Item"
        self.powerType = "fire"
        # pakai sprite yang sudah kamu tambahkan di JSON tadi
        self.image = spriteCollection["flower"].image  
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass
