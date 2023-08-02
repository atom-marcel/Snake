from gameobject import GameObject, GameObjectLoader
import pygame
from enum import Enum
from typing import Callable
from vector import Vector2D

class MouseState(Enum):
    MOUSE_OVER = 0
    MOUSE_OUT = 1
    CLICKED = 2

class MenuButton(GameObject):
    title: str
    textColor: pygame.Color
    hoverColor: pygame.Color
    callback: Callable
    mouseState: MouseState

    def __init__(self, title:str="", r:int=0, g:int=0, b:int=0):
        self.title = title
        self.textColor = pygame.Color(r, g, b)
        self.hoverColor = pygame.Color(0, 0, 0)
        self.callback = lambda: None

    def setHoverBackground(self, r:int, g:int, b:int):
        self.hoverColor = pygame.Color(r, g, b)
    
    def setCallback(self, cb:Callable):
        self.callback = cb

    def setTitle(self, title:str):
        self.title = title

    def setTextColor(self, r:int, g:int, b:int):
        self.color = pygame.Color(r, g, b)

    def checkMouseOver(self, x:int, y:int) -> MouseState:
        if(x > self.getX() and y > self.getY() and x < self.getX() + self.width and y < self.getY() + self.height):
            self.mouseState = MouseState.MOUSE_OVER
        else:
            self.mouseState = MouseState.MOUSE_OUT

    def handleEvents(self):
        from inputhandler import TheInputHandler
        x = TheInputHandler().mousePosition.getX()
        y = TheInputHandler().mousePosition.getY()
        self.checkMouseOver(x, y)
        leftMouseBtn = TheInputHandler().mouseBtnStates[0]

        if self.mouseState == MouseState.MOUSE_OVER and leftMouseBtn:
            self.callback()


    def update(self):
        self.handleEvents()
        self.render()
    
    def load(self, params: GameObjectLoader):
        return super().load(params)

    def render(self):
        from game import TheGame
        rect = pygame.Rect(self.getX(), self.getY(), self.width, self.height)
        textSurface = TheGame().font.render(self.title, True, self.textColor)

        # Draw background
        if(self.mouseState == MouseState.MOUSE_OUT):
            pygame.draw.rect(TheGame().surface, self.color, rect)
        if(self.mouseState == MouseState.MOUSE_OVER):
            pygame.draw.rect(TheGame().surface, self.hoverColor, rect)

        TheGame().surface.blit(textSurface, rect)