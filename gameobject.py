import pygame
from vector import Vector2D
from abc import ABC, abstractmethod

class GameObjectLoader(object):
    position: Vector2D
    velocity: Vector2D
    acceleration: Vector2D

    width: int
    height: int
    color: pygame.Color

    def __init__(self, x:int, y:int, width:int, height:int, r:int, g:int, b:int):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)
        self.width = width
        self.height = height
        self.color = pygame.Color(r, g, b)

class AbstractGameObject(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def render(self):
        pass

class GameObject(AbstractGameObject):
    position: Vector2D
    velocity: Vector2D
    acceleration: Vector2D

    width: int
    height: int
    color: pygame.Color

    def __init__(self):
        pass

    def getX(self) -> int:
        return self.position.x

    def getY(self) -> int:
        return self.position.y 

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.render()

    def load(self, params: GameObjectLoader):
        self.position = params.position
        self.velocity = params.velocity
        self.acceleration = params.acceleration
        self.width = params.width
        self.height = params.height
        self.color = params.color

    def render(self):
        from game import TheGame
        pygame.draw.rect(TheGame().surface, self.color, pygame.Rect(self.getX(), self.getY(), self.width, self.height))