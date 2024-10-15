import pygame
import time
import random

WIDTH, HEIGHT = 800, 725
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clue-Less")
scarletImg = pygame.image.load('miss scarlet.JPG')
colonelImg = pygame.image.load('colonel mustard.JPG')
greenImg = pygame.image.load('mr green.JPG')
peacockImg = pygame.image.load('mrs peacock.JPG')
whiteImg = pygame.image.load('mrs white.JPG')
plumImg = pygame.image.load('prof plum.JPG')

BG = pygame.transform.scale(pygame.image.load("gameboard.JPG"), (WIDTH, HEIGHT))



def draw():
    WIN.blit(BG, (0,0))
    WIN.blit(scarletImg,(WIDTH *.1,HEIGHT *.1))
    WIN.blit(colonelImg,(WIDTH *.4,HEIGHT *.1))
    WIN.blit(greenImg,(WIDTH *.7,HEIGHT *.1))
    WIN.blit(peacockImg,(WIDTH *.1,HEIGHT *.6))
    WIN.blit(whiteImg,(WIDTH *.4,HEIGHT *.6))
    WIN.blit(plumImg,(WIDTH *.7,HEIGHT *.6))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()



class Player:
    name = ""
    character = ""

weapons = ["Candlestick", "Wrench", "Lead Pipe", "Rope", "Dagger", "Revolver"]
rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
characters = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White"]

def joinGame():
    print("Welcome to Clue-Less! Please choose your character")

