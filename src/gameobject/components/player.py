from typing import List

import pygame

import vector
from gameobject.components.physics import RigidBodyComponent
from gameobject.components.spells import FireBallComponent
from gameobject.gameobject import DrawComponent, GameObject


class PlayerComponent(DrawComponent):
    def __init__(self, width: int, height: int, game_objects: List[GameObject]):
        super().__init__()
        self.width = width
        self.height = height
        self.game_objects = game_objects

        self.velocity = vector.Vector2D(0, 0)
        self.acceleration = vector.Vector2D(0, 0)

        self.texture = pygame.image.load('./resources/textures/player/standing.png')
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def draw(self, win: pygame.Surface):
        win.blit(self.texture, (self.game_object.position.x, self.game_object.position.y))
        pygame.draw.rect(win, (200, 25, 25),
                         (self.game_object.position.x, self.game_object.position.y, self.width, self.height), 5)

    def fire(self) -> GameObject:
        go = GameObject(vector.Vector2D(self.game_object.position.x, self.game_object.position.y))
        go.add_component(FireBallComponent(vector.Vector2D(10, 0), 25, 25))
        return go

    def update(self, delta_time: int):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_1]:
            self.game_objects.append(self.fire())
        if self.game_object.position.y >= 400:
            if keys_pressed[pygame.K_SPACE]:
                self.jump(vector.Vector2D(0, -10))

        if keys_pressed[pygame.K_LEFT]:
            self.game_object.position.x -= 5
        elif keys_pressed[pygame.K_RIGHT]:
            self.game_object.position.x += 5

    def jump(self, force: vector.Vector2D):
        (found, rbc) = self.game_object.get_component(RigidBodyComponent)
        if found:
            rbc.velocity.add(force)
