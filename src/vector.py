import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        if not isinstance(vec, Vector2D):
            raise Exception("vec needs to be of type Vector2D")

        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        if not isinstance(vec, Vector2D):
            raise Exception("vec needs to be of type Vector2D")

        self.x -= vec.x
        self.y -= vec.y

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        length = self.length()
        return Vector2D(self.x / length, self.y / length)


def sub(vec1: Vector2D, vec2: Vector2D):
    return Vector2D(vec1.x - vec2.x, vec1.y - vec2.y)
