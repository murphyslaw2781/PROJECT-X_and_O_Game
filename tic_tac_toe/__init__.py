#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Axe's and Oh's")
screen = pygame.display.set_mode((1000, 800),0,32)
font = pygame.font.SysFont('comicsansms', 35)
font_color = pygame.Color('white')
x = 500
y = 400

# Write on Screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text,1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Collect user input /Text Box
def header_message(text):
    draw_text(text,font, font_color, screen, x,y-200)
    
def main_menu():
    pass

def player():
    player_name = ''
    color_active = pygame.Color('gray15')
    color_passive = pygame.Color('white')
    color = color_active
    click = False
    while True:
        #RGB - Red, Blue, Green
        screen.fill((0,0,0))
        header_message('Player Name')
        #Mouse
        mx, my = pygame.mouse.get_pos()
        #Text Input Box
        button_1 = pygame.Rect(x-100, y-50, 200,50)
        pygame.draw.rect(screen,color, button_1)
        text_surface = font.render(player_name,True,(0,0,0))
        screen.blit(text_surface,(button_1.x+10,button_1.y))
        #Lets Play!
        button_3 = pygame.Rect(x-100, y+250, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text("Submit",font, (255, 255, 255), screen,x,y+270)
        
        if button_1.collidepoint((mx, my)):
            if click:
                color = color_passive
            else:
                color = color_active
        if button_3.collidepoint((mx, my)):
            if click:
                choose(player_name)
        # Menu Events             
       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == K_RETURN:
                    choose(player_name)
                else:
                    player_name += event.unicode
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def choose(player_name):
    
    click = False
    running = True
    while running:

        screen.fill((0,0,0))
        header_message('Welcome '+player_name)
        draw_text("Choose Your Player", font, (255, 255, 255), screen, x,y-50)
        
        mx, my = pygame.mouse.get_pos()
        
        # Avatars
        viking_image_click = pygame.Rect(x-55,y, 200, 200)
        viking_image = pygame.image.load('viking.png')
        screen.blit(viking_image,(x-35,y))

        viking_image2_click = pygame.Rect(x-300,y, 200, 200)
        viking_image2 = pygame.image.load('viking2.png')
        screen.blit(viking_image2,(x-255,y))

        viking_image3_click = pygame.Rect(x+150,y+10, 100, 200)
        viking_image3 = pygame.image.load('viking3.png')
        screen.blit(viking_image3,(x+150,y+10))

        #pygame.draw.rect(screen, (255, 255, 255), input_box)
        if viking_image_click.collidepoint((mx,my)):
            if click:
                character = pygame.image.load('viking.png')
                game(character)
        if viking_image2_click.collidepoint((mx,my)):
            if click:
                character = pygame.image.load('viking2.png')
                game(character)
        if viking_image3_click.collidepoint((mx,my)):
            if click:
                character = pygame.image.load('viking3.png')
                game(character)
        # Menu Buttons
        button_1 = pygame.Rect(x-100, y+250, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Play', font, (255, 255, 255), screen,x,y+270)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        # Text Input
        

        # Menu Events
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

def game(character):
    player_x = 485
    player_y = 700
    running = True
    click = False
    while running:

        screen.fill((0,0,0))
        screen.blit(character,(player_x,player_y))
        
        mx, my = pygame.mouse.get_pos()

        # Menu Events
        click=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_BACKSPACE:
                    running = False
                if event.key == K_LEFT:
                    player_x=player_x-50
                if event.key == K_RIGHT:
                    player_x = player_x+50
                if event.key == K_UP:
                    player_y = player_y-20
                if event.key == K_DOWN:
                    player_y = player_y+20
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

#Game Loop Written Below

player()
