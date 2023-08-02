# @Author: Marcel Maluta
# @Date:   2022-05-07T10:43:43+02:00
# @Email:  marcelmaluta@gmail.com
# @Last modified by:   Marcel Maluta
# @Last modified time: 2022-05-07T14:59:29+02:00

import math

class Vector2D(object):

    x: int
    y: int

    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y

    def add(self, x:int, y:int):
        self.x += x
        self.y += y

    def add_vector(self, vector:object):
        self.x += vector.x
        self.y += vector.y

    def set(self, x:int, y:int):
        self.x = x
        self.y = y

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y

    def getPoint(self) -> tuple:
        tuple = (self.x, self.y)
        return tuple

    def getLength(self) -> float:
        sum = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        return sum

    def printVector(self):
        print(f"({self.x}, {self.y})")

    def __add__(self, other: object) -> object:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> object:
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: int) -> object:
        return Vector2D(self.x * other, self.y * other)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def dot(self, other:object) -> int:
        return self.x * other.x + self.y * other.y

