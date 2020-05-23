from typing import List

import pygame

import vector
from gameobject.gameobject import DrawComponent, GameObject


# Change width and height to radius
class FireBallComponent(DrawComponent):
    def __init__(self, direction: vector.Vector2D, width: int, height: int, game_objects: List[GameObject],
                 origin: GameObject):
        super().__init__()
        self.direction = direction
        self.velocity = vector.Vector2D(0, 0)
        self.acceleration = vector.Vector2D(0, 0)

        self.game_objects = game_objects
        self.origin = origin
        self.width = width
        self.height = height
        self.texture = pygame.image.load('../resources/textures/spells/fireball.jpg').convert()
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def draw(self, win: pygame.Surface):
        win.blit(self.texture, (self.game_object.position.x, self.game_object.position.y))
        pygame.draw.rect(win, (200, 25, 25),
                         (self.game_object.position.x, self.game_object.position.y, self.width, self.height), 5)

    def update(self, delta_time: int):
        self.acceleration.add(self.direction)
        self.game_object.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.acceleration.mult(0)

        for go in self.game_objects:
            if not go == self.game_object and not go == self.origin:
                if self.game_object.position.x < go.position.x + 32 and self.game_object.position.x + self.width > go.position.x and self.game_object.position.y < go.position.y + 32 and self.game_object.position.y + self.height > go.position.y:
                    self.game_objects.remove(go)
