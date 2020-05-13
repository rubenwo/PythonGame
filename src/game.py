import pygame

import vector
from gameobject.components.enemy import EnemyComponent
from gameobject.components.environment import BrickComponent
from gameobject.components.movement import MoveToComponent
from gameobject.components.physics import RigidBodyComponent
from gameobject.components.player import PlayerComponent
from gameobject.components.spells import FireBallComponent
from gameobject.gameobject import GameObject

window_width = 500
window_height = 480

gravity = vector.Vector2D(0, 0.8)

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mario but better")

game_objects = []

bg = pygame.image.load('../resources/textures/background/bg.jpg').convert()

for n in range(3):
    for j in range(3):
        cube = GameObject(vector.Vector2D(window_width / 2 - (j * 32) + 100, window_height - 80 - (n * 32)))
        cube.add_component(BrickComponent(32, 32))
        cube.add_component(RigidBodyComponent(32, 32, game_objects, gravity, 1))
        game_objects.append(cube)

enemy = GameObject(vector.Vector2D(window_width / 2 - 100, window_height / 2))
enemy.add_component(EnemyComponent(64, 64))
enemy.add_component(MoveToComponent(vector.Vector2D(0, window_height - 64), 100))
enemy.add_component(RigidBodyComponent(64, 64, game_objects, gravity, 0.5))
game_objects.append(enemy)

player = GameObject(vector.Vector2D(window_width / 2, window_height / 2))
player.add_component(PlayerComponent(64, 64, game_objects))
player.add_component(RigidBodyComponent(64, 64, game_objects, gravity, 0.5))
game_objects.append(player)


# update the game objects
def update():
    delta_time = 30
    for go in game_objects:
        (found, bc) = go.get_component(FireBallComponent)
        if found:
            if go.position.x > window_width or go.position.x < 0:
                game_objects.remove(go)
        go.update(delta_time)


x = 0
rel_x = 0


# draw the background, player and cubes
def draw():
    win.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < window_width:
        win.blit(bg, (rel_x, 0))

    for go in game_objects:
        go.draw(win)
    pygame.display.update()


clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rel_x = x % bg.get_rect().width
    x -= 1
    update()
    draw()

    clock.tick(30)

pygame.quit()
