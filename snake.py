# @Author: Marcel Maluta
# @Date:   2022-05-07T12:30:03+02:00
# @Email:  marcelmaluta@gmail.com
# @Last modified by:   Marcel Maluta
# @Last modified time: 2022-05-07T16:04:40+02:00

from vector import Vector2D
from gameobject import GameObject, GameObjectLoader
import pygame
import time
import random
import array


class Snake(GameObject):
    body: list[GameObject]
    head: GameObject

    def __init__(self):
        from game import TheGame
        super().__init__()
        centerX = int(TheGame().window_x / 2)
        centerY = int(TheGame().window_y / 2)

        # Initialize Snake
        head = GameObject()
        head.load(GameObjectLoader(centerX, centerY, 10, 10, 0, 255, 0))
        body1 = GameObject()
        body1.load(GameObjectLoader(centerX+10, centerY, 10, 10, 0, 255, 0))
        body2 = GameObject()
        body2.load(GameObjectLoader(centerX+20, centerY, 10, 10, 0, 255, 0))

        self.head = head
        self.body = [self.head, body1, body2]
        self.head.velocity = Vector2D(-10, 0)
        self.position = self.body[0].position
        self.width = self.body[0].width
        self.height = self.body[0].height

    def ownCollision(self) -> bool:
        for bodyPart in self.body:
            if bodyPart == self.body[0]:
                continue
            if self.body[0].getX() == bodyPart.getX() and self.body[0].getY() == bodyPart.getY():
                from game import TheGame
                TheGame().gameOver()
                return True
        
        return False

    def checkBorderCollision(self) -> bool:
        from game import TheGame
        borderLeft = 0
        borderRight = TheGame().window_x
        borderTop = 0
        borderBottom = TheGame().window_y

        if self.body[0].getX() < borderLeft \
            or self.body[0].getX() > borderRight \
            or self.body[0].getY() < borderTop \
            or self.body[0].getY() > borderBottom:

                TheGame().gameOver()
                return True
        
        return False
    
    def handleEvents(self):
        from inputhandler import TheInputHandler, Keyboard
        if TheInputHandler().keyDown[Keyboard.UP]:
            self.body[0].velocity.set(0, -10)
        if TheInputHandler().keyDown[Keyboard.RIGHT]:
            self.body[0].velocity.set(10, 0)
        if TheInputHandler().keyDown[Keyboard.DOWN]:
            self.body[0].velocity.set(0, 10)
        if TheInputHandler().keyDown[Keyboard.LEFT]:
            self.body[0].velocity.set(-10, 0)

    def updateBody(self):
        self.body.reverse()
        for i, bodyPart in enumerate(self.body):
            if i+1 < len(self.body):
                bodyPart.position = self.body[i+1].position
        self.body.reverse()

    def addSegment(self):
        head = GameObject()
        newPos: Vector2D = self.body[0].position + self.body[0].velocity
        head.load(GameObjectLoader(self.body[0].position.x, self.body[0].position.y, 10, 10, 0 , 255, 0))
        head.velocity = self.body[0].velocity
        head.update()
        self.body[0].velocity.set(0, 0)
        self.body.insert(0, head)

    def update(self):
        from game import TheGame
        self.handleEvents()
        self.ownCollision()
        self.checkBorderCollision()
        self.updateBody()
        TheGame().clock.tick(10)
        for bodyPart in self.body:
            bodyPart.update()
        self.position = self.body[0].position