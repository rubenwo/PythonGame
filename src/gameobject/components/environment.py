from gameobject.gameobject import DrawComponent
import pygame


class BrickComponent(DrawComponent):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height
        self.texture = pygame.image.load('../resources/textures/environment/brick.jpg').convert()
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def draw(self, win: pygame.Surface):
        win.blit(self.texture, (self.game_object.position.x, self.game_object.position.y))
        pygame.draw.rect(win, (200, 25, 25),
                         (self.game_object.position.x, self.game_object.position.y, self.width, self.height), 5)

    def update(self, delta_time: int):
        pass
