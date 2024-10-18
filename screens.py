import pygame
import pygame_gui

WIDTH, HEIGHT = 800, 725
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clue-Less")
BG = pygame.transform.scale(pygame.image.load("images/gameboard.JPG"), (WIDTH*0.7, HEIGHT*0.7))

def draw_home_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Welcome to Clue-Less', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, 100))
    logo = pygame.image.load("images/digital-nomads.JPG")
    WIN.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2))
    return WIN

def draw_lobby():
    WIN.fill((0, 0, 0))
    return WIN

def draw_game_screen():
    WIN.fill((0, 0, 0))
    WIN.blit(BG, (WIDTH*0.15,HEIGHT*0.2))

def draw_end_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Game Over!', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))