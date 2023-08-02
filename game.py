import pygame
import time
from singleton import Singleton
from gamestatemachine import GameStateMachine
from gamestate import MainMenuState, GameOverState
from inputhandler import TheInputHandler

class TheGame(metaclass=Singleton):
    window_x: int = 720
    window_y: int = 480
    surface: pygame.Surface
    clock: pygame.time.Clock
    score: int
    
    score: int
    running: bool

    font: pygame.font.Font
    gameStateMachine: GameStateMachine

    def init(self):
        pygame.init()
        TheInputHandler().init()
        self.surface = pygame.display.set_mode((self.window_x, self.window_y))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 64)
        self.gameStateMachine = GameStateMachine()
        self.gameStateMachine.pushState(MainMenuState())
        self.running = True
        self.score = 0

    def handleEvents(self):
        TheInputHandler().update()

    def update(self):
        self.handleEvents()
        self.surface.fill(pygame.Color(0, 0, 0))
        self.gameStateMachine.update()
        pygame.display.flip()

    def quit(self):
        self.running = False

    def gameOver(self):
        self.gameStateMachine.changeState(GameOverState())

    def gameLoop(self):
        while(self.running):
            self.update()