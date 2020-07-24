#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Axe's and Oh's")
screen = pygame.display.set_mode((500, 500),0,32)
font = pygame.font.SysFont('comicsansms', 20)


# Write on Screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Collect user input /Text Box
def text_box():
    pass
    


def main_menu():
    player_name = ''
    color_active = pygame.Color('gray15')
    color_passive = pygame.Color('white')
    color = color_active
    click = False
    while True:
        #RGB - Red, Blue, Green
        screen.fill((0,0,0))
        
        # Menu Buttons
        mx, my = pygame.mouse.get_pos()
        #Text Input Box
        draw_text("Player Name",font, (255,255,255), screen, (100+(150/2)),(100+(50/2)))
        button_1 = pygame.Rect(150, 175, 200, 50)
        pygame.draw.rect(screen,color, button_1)
        #Text Render Player Name
        text_surface = font.render(player_name,True,(0,0,0))
        screen.blit(text_surface,(button_1.x+5,button_1.y+15))
        #Lets Play!
        button_3 = pygame.Rect(150, 400, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text("Play",font, (255, 255, 255), screen,225,415)
        
        if button_1.collidepoint((mx, my)):
            if click:
                color = color_passive
            else:
                color = color_active
        if button_3.collidepoint((mx, my)):
            if click:
                pass
        # Menu Events             
       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == K_RETURN:
                    choose()
                else:
                    player_name += event.unicode
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def choose():
    click = False
    running = True
    while running:

        screen.fill((0,0,0))
        draw_text('Welcome', font, (255, 255, 255), screen, (100+(200/2)),100)
        draw_text("Choose Your Player", font, (255, 255, 255), screen, (100+(120/2)),(100+(100/2)))
        
        mx, my = pygame.mouse.get_pos()
        
        # Text Box
        input_box = pygame.Rect(150, 200, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_box)
        if input_box.collidepoint((mx,my)):
            if click:
                pass

        # Menu Buttons
        button_1 = pygame.Rect(150, 400, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Submit', font, (255, 255, 255), screen, 215,415)
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        # Text Input
        

        # Menu Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
        
        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:

        screen.fill((0,0,0))
        draw_text('Welcome Player 2', font, (255, 255, 255), screen, 165,50)
        mx, my = pygame.mouse.get_pos()

        # Text Box
        input_box = pygame.Rect(150, 200, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_box)
        if input_box.collidepoint((mx,my)):
            if click:
                pass

        # Menu Buttons
        
        button_1 = pygame.Rect(150, 400, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Submit', font, (255, 255, 255), screen, 215,415)
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()

        # Menu Events
        click=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

#Game Loop Written Below

main_menu()
