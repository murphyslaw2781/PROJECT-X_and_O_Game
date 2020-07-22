#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Axe's and Oh's")
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont('comicsansms', 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text("Choose Your Player", font, (255, 255, 255), screen, 150, 50)

        mx, my = pygame.mouse.get_pos()

        draw_text("Player 1 Name",font, (255, 255, 255), screen, (100+(150/2)),(100+(50/2)))
        draw_text("Player 2 Name",font, (255, 255, 255), screen, (100+(150/2)),(200+(50/2)))
        
        button_1 = pygame.Rect(150, 100, 200, 50)
        button_2 = pygame.Rect(150, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                player1()
        if button_2.collidepoint((mx, my)):
            if click:
                player2()
        #Below draw the button squares if needed, I like hidden effect
        #pygame.draw.rect(screen, (255, 0, 0), button_1)
        #pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def player1():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Welcome Player 1', font, (255, 255, 255), screen, 150,50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def player2():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Welcome Player 2', font, (255, 255, 255), screen, 150,50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()