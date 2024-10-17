import pygame
import pygame_gui

WIDTH, HEIGHT = 800, 725
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clue-Less")
BG = pygame.transform.scale(pygame.image.load("images/gameboard.JPG"), (WIDTH*0.8, HEIGHT*0.8))

def draw_home_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Welcome to Clue-Less', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
    return WIN

def draw_lobby():
    WIN.fill((0, 0, 0))
    return WIN

def draw_game_screen():
    WIN.blit(BG, (WIDTH*0.1,HEIGHT*0.1))

def draw_end_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Game Over!', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))