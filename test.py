import pygame
import pymunk  # Import pymunk...

window_width = 852
window_height = 480

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mario but better")

bg = pygame.image.load('./resources/textures/background/bg.jpg').convert()

space = pymunk.Space()  # Create a Space which contain the simulation
space.gravity = 0, 1000  # Set its gravity

body = pymunk.Body(1, 1666)  # Create a Body with mass and moment
body.position = 50, 0  # Set th# e position of the body

poly = pymunk.Poly.create_box(body)  # Create a box shape and attach to body
space.add(body, poly)  # Add both body and shape to the simulation


# update the game objects
def update():
    delta_time = 30
    space.step(0.02)  # Step the simulation one step forward
    print(body.position)


# draw the background, player and cubes
def draw():
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (200, 25, 25), (body.position.x, body.position.y, 25, 25))
    pygame.display.update()


clock = pygame.time.Clock()

running = True
while running:  # Infinite loop simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
    draw()

    clock.tick(30)
