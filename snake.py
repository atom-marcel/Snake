# @Author: Marcel Maluta
# @Date:   2022-05-07T12:30:03+02:00
# @Email:  marcelmaluta@gmail.com
# @Last modified by:   Marcel Maluta
# @Last modified time: 2022-05-07T16:04:40+02:00

from vector import Vector
import pygame
import random

class Snake(object):
    def __init__(self, x, y):
        self.body = [Vector(x,y), Vector(x+10, y), Vector(x+20, y), Vector(x+30, y)]
        self.current_speed = Vector(-10, 0)

    def move(self):
        self.body.pop(len(self.body) - 1)
        self.body.insert(0, Vector(self.body[0].x+self.current_speed.x, self.body[0].y+self.current_speed.y))

    def move_to(self, movement):
        if movement == "LEFT":
            self.current_speed.set(-10, 0)
        if movement == "RIGHT":
            self.current_speed.set(10, 0)
        if movement == "UP":
            self.current_speed.set(0, -10)
        if movement == "DOWN":
            self.current_speed.set(0, 10)

    def draw(self, surface):
        for v in self.body:
            pygame.draw.rect(surface, pygame.Color(255, 255, 255), (v.x, v.y, 10, 10))
            pygame.draw.rect(surface, pygame.Color(87, 212, 106), (v.x+1, v.y+1, 8, 8))

    def add_segment(self):
        first_segment = self.body[0]
        x = first_segment.x + self.current_speed.x
        y = first_segment.y + self.current_speed.y
        self.body.insert(0, Vector(x, y))

    def check_own_collision(self):
        for i in range(1, len(self.body) - 1):
            if self.body[i].x == self.get_head().x and self.body[i].y == self.get_head().y:
                return True
        return False

    def get_head(self):
        return self.body[0]

class Fruit(object):
    def __init__(self, x, y):
        self.position = Vector(x, y)

    def set_position(self, x, y):
        self.position.set(x, y)

    def set_random_position(self, max_x, max_y):
        self.set_position(random.randrange(1, (max_x//10)) * 10, random.randrange(1, (max_y//10)) * 10)

    def get_point(self):
        tuple = (self.position.x, self.position.y)
        return tuple

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color(235, 61, 44), (self.position.x, self.position.y, 10, 10))
