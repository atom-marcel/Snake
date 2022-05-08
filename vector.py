# @Author: Marcel Maluta
# @Date:   2022-05-07T10:43:43+02:00
# @Email:  marcelmaluta@gmail.com
# @Last modified by:   Marcel Maluta
# @Last modified time: 2022-05-07T14:59:29+02:00

import math

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def add_vector(self, vector):
        self.x += vector.x
        self.y += vector.y

    def set(self, x, y):
        self.x = x
        self.y = y

    def scalar(self, a):
        self.x = self.x * a
        self.y = self.y * a

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_point(self):
        tuple = (self.x, self.y)
        return tuple

    def get_length(self):
        sum = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        return sum

    def print_vector(self):
        print(f"({self.x}, {self.y})")

if __name__ == '__main__':
    v = Vector(13, 12)
    print(str(v.get_length()))
