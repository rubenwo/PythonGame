import pygame
import vector
from typing import List


class Component(object):
    def __init__(self):
        self.game_object: GameObject = {}
        pass

    def set_game_object(self, game_object):
        if not isinstance(game_object, GameObject):
            raise Exception("game_object needs to be of type 'GameObject'")
        self.game_object = game_object

    def update(self, delta_time: int):
        pass


class DrawComponent(Component):
    def __init__(self):
        super().__init__()

    def draw(self, win: pygame.Surface):
        pass

    def update(self, delta_time: int):
        pass


class GameObject(object):
    def __init__(self, position: vector.Vector2D):
        self.position = position
        self.components: List[Component] = []
        self.draw_component = None

    def add_component(self, component: Component):
        component.set_game_object(self)
        self.components.append(component)
        if self.draw_component is None:
            if isinstance(component, DrawComponent):
                self.draw_component = component

    def get_components(self):
        return self.components

    def get_component(self, c) -> (bool, Component):
        for comp in self.components:
            if isinstance(comp, c):
                return True, comp
        return False, None

    def draw(self, win: pygame.Surface):
        if self.draw_component is None:
            return
        self.draw_component.draw(win=win)

    def update(self, delta_time: int):
        for comp in self.components:
            comp.update(delta_time)
