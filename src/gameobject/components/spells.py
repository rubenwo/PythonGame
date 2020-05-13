import pygame

import vector
from gameobject.gameobject import DrawComponent


# Change width and height to radius
class FireBallComponent(DrawComponent):
    def __init__(self, direction: vector.Vector2D, width: int, height: int):
        super().__init__()
        self.direction = direction
        self.velocity = vector.Vector2D(0, 0)
        self.acceleration = vector.Vector2D(0, 0)

        self.width = width
        self.height = height
        self.texture = pygame.image.load('../resources/textures/spells/fireball.jpg')
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
