import random
from typing import List

import vector
from gameobject.gameobject import Component, GameObject


class RigidBodyComponent(Component):
    def __init__(self, width: int, height: int, game_objects: List[GameObject], gravity: vector.Vector2D, mass: float):
        super().__init__()
        self.width = width
        self.height = height
        self.game_objects = game_objects

        self.mass = mass

        self.gravity = gravity
        self.velocity = vector.Vector2D(0, 0)
        self.acceleration = vector.Vector2D(0, 0)

    def update(self, delta_time: int):
        for obj in self.game_objects:
            if not obj == self.game_object:
                (found, rigid_body_comp) = obj.get_component(RigidBodyComponent)
                if found:
                    (col, col_pos) = rigid_body_collision(self, rigid_body_comp)
                    # TODO: Add correct physics interaction
                    if col and self.mass <= rigid_body_comp.mass:
                        self.game_object.position.x += random.randint(-10, 10)

        self.acceleration.add(self.gravity)
        self.game_object.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.acceleration.mult(0)
        if self.game_object.position.y >= 400:
            self.velocity.y = 0

    def apply_force(self, force: vector.Vector2D):
        self.acceleration.add(force)


def rigid_body_collision(obj1: RigidBodyComponent, obj2: RigidBodyComponent) -> (bool, vector.Vector2D):
    collision = obj1.game_object.position.x < obj2.game_object.position.x + obj2.width and \
                obj1.game_object.position.x + obj1.width > obj2.game_object.position.x and \
                obj1.game_object.position.y < obj2.game_object.position.y + obj2.height and \
                obj1.game_object.position.y + obj1.height > obj2.game_object.position.y

    collision_point = vector.Vector2D(0, 0)
    return collision, collision_point
