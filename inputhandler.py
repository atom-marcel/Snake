from singleton import Singleton
from vector import Vector2D
from typing import Literal
from enum import Enum
import pygame

class Keyboard(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    ESC = 4

class TheInputHandler(metaclass=Singleton):
    mousePosition: Vector2D
    mouseBtnStates: Literal[3]

    keyDown: dict[Keyboard, bool]

    def init(self):
        self.reset()

    def reset(self):
        self.mousePosition = Vector2D(0, 0)
        self.mouseBtnStates = (False, False, False)
        
        self.keyDown = {}

        # Init keyboard states
        for key in Keyboard:
            self.keyDown[key] = False
    
    def getMouseBtnStates(self) -> Literal[3]:
       return self.mouseBtnStates

    def getMousePosition(self) -> Vector2D:
        return self.mousePosition

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                self.mousePosition.set(x, y)

            if event.type == pygame.QUIT:
                import game
                game.TheGame().gameStateMachine.popState()
                game.TheGame().quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseBtnStates = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseBtnStates = pygame.mouse.get_pressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.keyDown[Keyboard.UP] = True
                if event.key == pygame.K_RIGHT:
                    self.keyDown[Keyboard.RIGHT] = True
                if event.key == pygame.K_DOWN:
                    self.keyDown[Keyboard.DOWN] = True
                if event.key == pygame.K_LEFT:
                    self.keyDown[Keyboard.LEFT] = True
                if event.key == pygame.K_ESCAPE:
                    self.keyDown[Keyboard.ESC] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.keyDown[Keyboard.UP] = False
                if event.key == pygame.K_RIGHT:
                    self.keyDown[Keyboard.RIGHT] = False
                if event.key == pygame.K_DOWN:
                    self.keyDown[Keyboard.DOWN] = False
                if event.key == pygame.K_LEFT:
                    self.keyDown[Keyboard.LEFT] = False
                if event.key == pygame.K_ESCAPE:
                    self.keyDown[Keyboard.ESC] = False
