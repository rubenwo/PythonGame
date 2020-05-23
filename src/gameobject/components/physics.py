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

        self.gravity = vector.Vector2D(gravity.x, gravity.y)
        self.velocity = vector.Vector2D(0, 0)
        self.acceleration = vector.Vector2D(0, 0)

    def update(self, delta_time: int):
        self.acceleration.add(self.gravity)
        self.game_object.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.acceleration.mult(0)
        for obj in self.game_objects:
            if not obj == self.game_object:
                (found, rigid_body_comp) = obj.get_component(RigidBodyComponent)
                if found:
                    # TODO: Add correct physics interaction
                    if bounding_box_collision_x(self, rigid_body_comp) and self.mass <= rigid_body_comp.mass:
                        self.velocity.x = 0
                    if bounding_box_collision_y(self, rigid_body_comp) and self.mass <= rigid_body_comp.mass:
                        if self.game_object.position.y > obj.position.y:
                            self.game_object.position.y = obj.position.y + rigid_body_comp.height + 5
                            self.velocity.y = 0.001
                        else:
                            self.velocity.y = 0

    def apply_force(self, force: vector.Vector2D):
        self.acceleration.add(force)


def bounding_box_collision_x(obj1: RigidBodyComponent, obj2: RigidBodyComponent) -> bool:
    collision = obj1.game_object.position.x + obj1.width + obj1.velocity.x > obj2.game_object.position.x and \
                obj1.game_object.position.x + obj1.velocity.x < obj2.game_object.position.x + obj2.width and \
                obj1.game_object.position.y + obj1.height > obj2.game_object.position.y and \
                obj1.game_object.position.y < obj2.game_object.position.y + obj2.height
    return collision


def bounding_box_collision_y(obj1: RigidBodyComponent, obj2: RigidBodyComponent) -> bool:
    collision = obj1.game_object.position.x + obj1.width > obj2.game_object.position.x and \
                obj1.game_object.position.x < obj2.game_object.position.x + obj2.width and \
                obj1.game_object.position.y + obj1.height + obj1.velocity.y > obj2.game_object.position.y and \
                obj1.game_object.position.y + obj1.velocity.y < obj2.game_object.position.y + obj2.height
    return collision
