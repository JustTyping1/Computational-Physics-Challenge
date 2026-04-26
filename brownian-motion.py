# Importing libraries
import pygame
import pymunk
import random
import numpy as np


# Setup
GameDisplay = pygame.display.set_mode((600,600))
pygame.display.set_caption("Brownian Motion")
clock = pygame.time.Clock()
space = pymunk.Space()

FPS = 60 # Frame rate
e = 1 # Elasticity
R = 20 # Radius of big particle
r = 5 # Radius of small particle
rho = 1 # Density of big particle
n = 500 # Number of little particles
T = 100000 # Temperature
points = [] # Tracking points where the large particle goes

# Start position for large particle
x_start = random.randint(0, 600)
y_start = random.randint(0, 600)

# Defining class of wall of container
class Wall():
    def __init__(self, point1, point2):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC) # Create a static body for the walls of the container
        self.shape = pymunk.Segment(self.body, point1, point2, 5) # 
        self.shape.elasticity = e
        space.add(self.body, self.shape)

# Defining class of large particle
class BigParticle():
    def __init__(self, position):
        self.position = position
        self.body = pymunk.Body()
        self.body.position = self.position[0], self.position[1]
        self.body.velocity = 0, 0
        self.shape = pymunk.Circle(self.body, R)
        self.shape.density = rho
        self.shape.elasticity = e
        space.add(self.body, self.shape)
    def draw(self):
            x, y = self.body.position
            pygame.draw.circle(GameDisplay, (255, 0, 0), (int(x), int(y)), R)

# Defining class of small particles
class LittleParticle():
    def __init__(self, position):
        self.position = position
        self.body = pymunk.Body()
        self.body.position = self.position[0], self.position[1]
        self.body.velocity = random.uniform(-np.sqrt(T)/np.sqrt(2), np.sqrt(T)/np.sqrt(2)), random.uniform(-np.sqrt(T)/np.sqrt(2), np.sqrt(T)/np.sqrt(2))
        self.shape = pymunk.Circle(self.body, r)
        self.shape.density = rho
        self.shape.elasticity = e
        space.add(self.body, self.shape)

    def draw(self):
            x, y = self.body.position
            pygame.draw.circle(GameDisplay, (255, 255, 255), (int(x), int(y)), r)

# Where to draw walls
walls = [Wall((0,0), (0,600)),
         Wall((0,0), (600,0)),
         Wall((0,600), (600,600)),
         Wall((600,0), (600,600))]

# Where to draw particles
particles = [LittleParticle(position = (random.randint(0, 600), random.randint(0, 600))) for i in range(n)]
bulk_particle = BigParticle(position=(x_start, y_start))

# Main game loop
going = True

while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    
    clock.tick(FPS)
    GameDisplay.fill((0, 0, 0))

    points.append(tuple(bulk_particle.body.position)) # Adding latest position of large particle

    for particle in particles:
        particle.draw()

    # Drawing in trail for large particle
    if len(points) > 1:
        pygame.draw.lines(GameDisplay, (135, 206, 250), False, points, 1)

    bulk_particle.draw()

    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)
    
pygame.quit()

# Simulation inspired by Python-Brownian-Motion by Prithvi Ramrucha (https://github.com/prithvi-ramrucha/Python-Brownian-Motion)
# Modified and extended for BPhO Computational Physics Challenge 2026