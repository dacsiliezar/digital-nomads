import pygame
import pygame_gui
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
    clock = pygame.time.Clock()
    run = True
    active = False
    game_state = "home_screen"
    white = pygame.Color('white')
    color_passive = pygame.Color('gray15')
    color_active = pygame.Color('lightskyblue3')
    color = color_passive
    name = 'Type name'
    title = 'Please select your character'
    font = pygame.font.SysFont('comicsansms',40)
    name_box = pygame.Rect(250,725/2,300,50)
    while run:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                run = False
                break


            if game_state == "home_screen":
                screens.draw_home_screen()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE]:
                    player_x = 200
                    player_y = 400
                    game_state = "lobby"
                    game_over = False


            elif game_state == "lobby":
                WIN = screens.draw_lobby()
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                scarlet_button = classes.ImageButton(image=pygame.image.load("images/miss scarlet.JPG"), pos=(800*.25, 725*.25), name="Miss Scarlet")
                colonel_button = classes.ImageButton(image=pygame.image.load("images/colonel mustard.JPG"), pos=(800*.5, 725*.25), name="Colonel Mustard")
                green_button = classes.ImageButton(image=pygame.image.load("images/mr green.JPG"), pos=(800*.75, 725*.25), name="Mr. Green")
                peacock_button = classes.ImageButton(image=pygame.image.load("images/mrs peacock.JPG"), pos=(800*.25, 725*.75), name="Mrs. Peacock")
                white_button = classes.ImageButton(image=pygame.image.load("images/mrs white.JPG"), pos=(800*.5, 725*.75), name="Mrs. White")
                plum_button = classes.ImageButton(image=pygame.image.load("images/prof plum.JPG"), pos=(800*.75, 725*.75), name="Professor Plum")
                for button in [scarlet_button, colonel_button, green_button, peacock_button, white_button, plum_button]:
                    button.update(WIN)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in [scarlet_button, colonel_button, green_button, peacock_button, white_button, plum_button]:
                        if button.checkForInput(MENU_MOUSE_POS):
                            title = 'Youve selected ' + button.name
                    if name_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                    color = color_active if active else color_passive
                if event.type == (pygame.KEYDOWN or pygame.TEXTINPUT):
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            name += event.unicode
                pygame.draw.rect(WIN,color,name_box,3)
                surf = font.render(name,True,color)
                titlerend = font.render(title, True, (255, 255, 255))
                WIN.blit(surf,(name_box.x+5, name_box.y-5))
                WIN.blit(titlerend,(400-titlerend.get_width()/2,300))
                name_box.w = max(300, surf.get_width()+10)
                if event.type == pygame.K_SPACE:
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
        
        clock.tick(120)
    pygame.quit()

if __name__ == "__main__":
    main()

