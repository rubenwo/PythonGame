import pygame

from gameobject.components.movement import MoveToComponent
from gameobject.gameobject import DrawComponent


class EnemyComponent(DrawComponent):
    def __init__(self, width: int, height: int):
        super().__init__()

        self.width = width
        self.height = height

        self.texture = pygame.image.load('../resources/textures/enemy/enemy.png').convert()
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def draw(self, win: pygame.Surface):
        win.blit(self.texture, (self.game_object.position.x, self.game_object.position.y))
        pygame.draw.rect(win, (200, 25, 25),
                         (self.game_object.position.x, self.game_object.position.y, self.width, self.height), 5)

    def update(self, delta_time: int):
        (found, moveTo) = self.game_object.get_component(MoveToComponent)
        if found:
            if moveTo.destination.x == self.game_object.position.x and moveTo.destination.y == self.game_object.position.y:
                if moveTo.destination.x == 500 - self.width:
                    moveTo.destination.x = 0
                else:
                    moveTo.destination.x = 500 - self.width
