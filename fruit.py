from gameobject import GameObject
from vector import Vector2D
import pygame
import random

class Fruit(GameObject):
    
    def setPosition(self, x, y):
        self.position.set(x, y)

    def setRandomPosition(self, max_x, max_y):
        self.setPosition(random.randrange(1, (max_x//10)) * 10, random.randrange(1, (max_y//10)) * 10)

    def getPoint(self):
        tuple = (self.position.x, self.position.y)
        return tuple

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color(235, 61, 44), (self.position.x, self.position.y, 10, 10))
