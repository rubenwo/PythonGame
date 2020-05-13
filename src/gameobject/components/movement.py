import vector
from gameobject.gameobject import Component


class MoveToComponent(Component):
    def __init__(self, destination: vector.Vector2D, speed: int):
        super().__init__()
        self.destination = destination
        self.speed = speed

    def update(self, delta_time: int):
        dt = delta_time / 1000
        diff = vector.sub(self.destination, self.game_object.position)
        if diff.length() > self.speed * dt:
            diff = diff.normalized()

            self.game_object.position.x = self.game_object.position.x + self.speed * diff.x * dt
            self.game_object.position.y = self.game_object.position.y + self.speed * diff.y * dt
        else:
            self.game_object.position.x = self.destination.x
            self.game_object.position.y = self.destination.y
