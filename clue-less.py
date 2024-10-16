import pygame
import time
import random
import screens
import functions
import classes

pygame.init()

global WIDTH, HEIGHT
global WIN
global start_button


def main():
    run = True
    game_state = "home_screen"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if game_state == "home_screen":
            screens.draw_home_screen()
            keyhit = pygame
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                player_x = 200
                player_y = 400
                game_state = "lobby"
                game_over = False
        elif game_state == "lobby":
            screens.draw_lobby()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                player_x = 200
                player_y = 400
                game_state = "game_screen"
                game_over = False
        elif game_state == "game_screen":
            screens.draw_game_screen()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                player_x = 200
                player_y = 400
                game_state = "end_screen"
                game_over = False
        elif game_state == "end_screen":
            screens.draw_end_screen()
    pygame.quit()

if __name__ == "__main__":
    main()

