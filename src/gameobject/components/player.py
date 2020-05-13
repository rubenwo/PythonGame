from enum import Enum
from typing import List

import pygame

import vector
from gameobject.components.physics import RigidBodyComponent
from gameobject.components.spells import FireBallComponent
from gameobject.gameobject import DrawComponent, GameObject


class Direction(Enum):
    Zero = 0
    Right = 1
    Left = 2


class PlayerComponent(DrawComponent):
    def __init__(self, width: int, height: int, game_objects: List[GameObject]):
        super().__init__()
        self.width = width
        self.height = height
        self.game_objects = game_objects

        self.direction = Direction.Zero

        self.texture = [
            pygame.image.load('../resources/textures/player/standing.png'),
            pygame.image.load('../resources/textures/player/L1.png'),
            pygame.image.load('../resources/textures/player/L2.png'),
            pygame.image.load('../resources/textures/player/L3.png'),
            pygame.image.load('../resources/textures/player/L4.png'),
            pygame.image.load('../resources/textures/player/R1.png'),
            pygame.image.load('../resources/textures/player/R2.png'),
            pygame.image.load('../resources/textures/player/R3.png'),
            pygame.image.load('../resources/textures/player/R4.png'),
        ]
        for tex in self.texture:
            tex = pygame.transform.scale(tex, (self.width, self.height))
        self.texture_index = 0

        self.speed = 5

    def draw(self, win: pygame.Surface):
        win.blit(self.texture[self.texture_index],
                 (self.game_object.position.x - self.width / 2, self.game_object.position.y))
        pygame.draw.rect(win, (200, 25, 25),
                         (self.game_object.position.x, self.game_object.position.y, self.width, self.height), 5)

    def fire(self) -> GameObject:
        go = GameObject(
            vector.Vector2D(self.game_object.position.x + self.width + 10,
                            self.game_object.position.y + self.height / 2))
        direction = vector.Vector2D(10, 0)
        if self.direction == Direction.Left:
            direction.x *= -1
            go.position.x -= self.width * 2 - 10
        go.add_component(FireBallComponent(direction, 25, 25))
        return go

    def update(self, delta_time: int):
        keys_pressed = pygame.key.get_pressed()

        (found, rbc) = self.game_object.get_component(RigidBodyComponent)

        speed_mul = 1
        if keys_pressed[pygame.K_LSHIFT]:
            speed_mul = 1.5

        if keys_pressed[pygame.K_1]:
            self.game_objects.append(self.fire())
        if found and rbc.velocity.y == 0:
            if keys_pressed[pygame.K_SPACE]:
                self.jump(vector.Vector2D(0, -10))
        if found:
            if rbc.velocity.x > 0:
                rbc.velocity.x -= 1 * speed_mul
            elif rbc.velocity.x < 0:
                rbc.velocity.x += 1 * speed_mul

        if keys_pressed[pygame.K_LEFT]:
            self.direction = Direction.Left
            if found:
                if not rbc.velocity.x < -self.speed:
                    rbc.apply_force(vector.Vector2D(-self.speed * speed_mul, 0))
        elif keys_pressed[pygame.K_RIGHT]:
            self.direction = Direction.Right
            if found:
                if not rbc.velocity.x > self.speed:
                    rbc.apply_force(vector.Vector2D(self.speed * speed_mul, 0))
        else:
            self.direction = Direction.Zero

        self.texture_index += 1
        if self.direction == Direction.Zero:
            self.texture_index = 0
        elif self.direction == Direction.Left:
            if self.texture_index > 4:
                self.texture_index = 1
        else:
            if self.texture_index > 8 or self.texture_index < 5:
                self.texture_index = 5

    def jump(self, force: vector.Vector2D):
        (found, rbc) = self.game_object.get_component(RigidBodyComponent)
        if found:
            print("jump")
            rbc.velocity.add(force)
