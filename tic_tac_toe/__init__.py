__version__ = '0.1.0'
import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1200,600))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

