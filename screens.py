import pygame
import pygame_gui

WIDTH, HEIGHT = 800, 725
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clue-Less")
scarletImg = pygame.image.load('images/miss scarlet.JPG')
colonelImg = pygame.image.load('images/colonel mustard.JPG')
greenImg = pygame.image.load('images/mr green.JPG')
peacockImg = pygame.image.load('images/mrs peacock.JPG')
whiteImg = pygame.image.load('images/mrs white.JPG')
plumImg = pygame.image.load('images/prof plum.JPG')
BG = pygame.transform.scale(pygame.image.load("images/gameboard.JPG"), (WIDTH, HEIGHT))

def draw_home_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Welcome to Clue-Less', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
    WIN.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 + start_button.get_height()/2))
    pygame.display.update()

def draw_lobby():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Please Select Your Character', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, 0.4*HEIGHT))
    #WIN.blit(scarletImg,(WIDTH *.1,HEIGHT *.1))
    WIN.blit(colonelImg,(WIDTH *.4,HEIGHT *.1))
    WIN.blit(greenImg,(WIDTH *.7,HEIGHT *.1))
    WIN.blit(peacockImg,(WIDTH *.1,HEIGHT *.6))
    WIN.blit(whiteImg,(WIDTH *.4,HEIGHT *.6))
    WIN.blit(plumImg,(WIDTH *.7,HEIGHT *.6))
    pygame.display.update()
    return WIN

def draw_game_screen():
    WIN.blit(BG, (0,0))
    pygame.display.update()

def draw_end_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Game Over!', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
    pygame.display.update()
