from abc import ABC, abstractmethod
from typing import List
from gamestate import GameState
import pygame
from inputhandler import TheInputHandler

class GameStateMachine(object):
    from gamestate import GameState
    gameStates: List[GameState]

    def __init__(self) -> None:
        self.gameStates = list[GameState]()

    def popState(self):
        self.gameStates[-1].onExit()
        self.gameStates.pop()

    def changeState(self, state:GameState):
        print(self.gameStates)
        self.popState()
        self.gameStates.append(state)
        TheInputHandler().reset()
        self.gameStates[-1].onEnter()

    def pushState(self, state:GameState):
        self.gameStates.append(state)
        TheInputHandler().reset()
        self.gameStates[-1].onEnter()

    def update(self):
        if len(self.gameStates) > 0:
            self.gameStates[-1].update()