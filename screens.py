import pygame
import classes

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
    lobby_button = classes.ImageButton(image=pygame.image.load("images/join lobby button.png"), pos=(800*.5, 725*.8), name="Join Lobby")
    lobby_button.update(WIN)
    return WIN, lobby_button

def draw_lobby():
    WIN.fill((0, 0, 0))
    lobby_buttons = []
    scarlet_button = classes.ImageButton(image=pygame.image.load("images/miss scarlet.JPG"), pos=(800*.25, 725*.25), name="Miss Scarlet")
    colonel_button = classes.ImageButton(image=pygame.image.load("images/colonel mustard.JPG"), pos=(800*.5, 725*.25), name="Colonel Mustard")
    green_button = classes.ImageButton(image=pygame.image.load("images/mr green.JPG"), pos=(800*.75, 725*.25), name="Mr. Green")
    peacock_button = classes.ImageButton(image=pygame.image.load("images/mrs peacock.JPG"), pos=(800*.25, 725*.75), name="Mrs. Peacock")
    white_button = classes.ImageButton(image=pygame.image.load("images/mrs white.JPG"), pos=(800*.5, 725*.75), name="Mrs. White")
    plum_button = classes.ImageButton(image=pygame.image.load("images/prof plum.JPG"), pos=(800*.75, 725*.75), name="Professor Plum")
    player_button = classes.ImageButton(image=pygame.image.load("images/add player button.png"), pos=(800*.3, 680), name="Add Player")
    start_button = classes.ImageButton(image=pygame.image.load("images/start game button.png"), pos=(800*.7, 680), name="Start Game")
    lobby_buttons = [scarlet_button,colonel_button,green_button,peacock_button,white_button,plum_button]
    for button in lobby_buttons:
        button.update(WIN)
    player_button.update(WIN)
    start_button.update(WIN)
    return WIN, lobby_buttons, player_button, start_button

def draw_game_screen():
    WIN.fill((0, 0, 0))
    WIN.blit(BG, (WIDTH*0.15,HEIGHT*0.2))
    move_button = classes.ImageButton(image=pygame.image.load("images/move-player.png"), pos=(800*.3, 680), name="Move Player")
    end_button = classes.ImageButton(image=pygame.image.load("images/end-turn.png"), pos=(800*.7, 680), name="End Turn")
    suggestion_button = classes.ImageButton(image=pygame.image.load("images/make-suggestion.png"), pos=(800*.3, 45), name="Make Suggestion")
    accusation_button = classes.ImageButton(image=pygame.image.load("images/make-accusation.png"), pos=(800*.7, 45), name="Make Accusation")
    for button in [move_button, end_button, suggestion_button, accusation_button]:
        button.update(WIN)
    return move_button, end_button, suggestion_button, accusation_button

def draw_end_screen():
    WIN.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    title = font.render('Game Over!', True, (255, 255, 255))
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))