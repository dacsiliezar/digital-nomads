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
    color_active = pygame.Color('green2')
    color = color_passive
    name = "Type Name"
    title = 'Please select your character'
    font = pygame.font.SysFont('comicsansms',40)
    name_box = pygame.Rect(250,725/2,300,50)
    game_players = []
    curr_char = ""
    #locations = classes.Location()
    #print(vars(locations.rooms))
    #print(vars(locations.roomX))
    #print(vars(locations.roomY))
    while run:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                run = False
                break
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            if game_state == "home_screen":
                WIN = screens.draw_home_screen()
                lobby_button = classes.ImageButton(image=pygame.image.load("images/join lobby button.png"), pos=(800*.5, 725*.8), name="Join Lobby")
                lobby_button.update(WIN)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if lobby_button.checkForInput(MENU_MOUSE_POS):
                        player_x = 200
                        player_y = 400
                        game_state = "lobby"
                        game_over = False

            elif game_state == "lobby":
                WIN = screens.draw_lobby()
                scarlet_button = classes.ImageButton(image=pygame.image.load("images/miss scarlet.JPG"), pos=(800*.25, 725*.25), name="Miss Scarlet")
                colonel_button = classes.ImageButton(image=pygame.image.load("images/colonel mustard.JPG"), pos=(800*.5, 725*.25), name="Colonel Mustard")
                green_button = classes.ImageButton(image=pygame.image.load("images/mr green.JPG"), pos=(800*.75, 725*.25), name="Mr. Green")
                peacock_button = classes.ImageButton(image=pygame.image.load("images/mrs peacock.JPG"), pos=(800*.25, 725*.75), name="Mrs. Peacock")
                white_button = classes.ImageButton(image=pygame.image.load("images/mrs white.JPG"), pos=(800*.5, 725*.75), name="Mrs. White")
                plum_button = classes.ImageButton(image=pygame.image.load("images/prof plum.JPG"), pos=(800*.75, 725*.75), name="Professor Plum")
                player_button = classes.ImageButton(image=pygame.image.load("images/add player button.png"), pos=(800*.3, 680), name="Add Player")
                start_button = classes.ImageButton(image=pygame.image.load("images/start game button.png"), pos=(800*.7, 680), name="Start Game")
                for button in [scarlet_button, colonel_button, green_button, peacock_button, white_button, plum_button, start_button, player_button]:
                    button.update(WIN)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in [scarlet_button, colonel_button, green_button, peacock_button, white_button, plum_button]:
                        if button.checkForInput(MENU_MOUSE_POS):
                            title = 'Youve selected ' + button.name
                            curr_char = button.name
                    if player_button.checkForInput(MENU_MOUSE_POS):
                        game_players.append(classes.Player(name, curr_char))
                        functions.printPlayers(game_players)
                        title = "Player Added!"
                        name = "Type Name"
                    if start_button.checkForInput(MENU_MOUSE_POS):
                        player_x = 200
                        player_y = 400
                        game_state = "game_screen"
                        game_over = False
                    if name_box.collidepoint(event.pos):
                        active = True
                        if name == "Type Name":
                            name = ""
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
                surf = font.render(name,True,(255,255,255))
                titlerend = font.render(title, True, (255, 255, 255))
                WIN.blit(surf,(name_box.x+5, name_box.y-5))
                WIN.blit(titlerend,(400-titlerend.get_width()/2,300))
                name_box.w = max(300, surf.get_width()+10)

            elif game_state == "game_screen":
                #print(pygame.mouse.get_pos())
                screens.draw_game_screen()
                move_button = classes.ImageButton(image=pygame.image.load("images/move-player.png"), pos=(800*.3, 680), name="Move Player")
                end_button = classes.ImageButton(image=pygame.image.load("images/end-turn.png"), pos=(800*.7, 680), name="End Turn")
                suggestion_button = classes.ImageButton(image=pygame.image.load("images/make-suggestion.png"), pos=(800*.3, 45), name="Make Suggestion")
                accusation_button = classes.ImageButton(image=pygame.image.load("images/make-accusation.png"), pos=(800*.7, 45), name="Make Accusation")
                for button in [move_button, end_button, suggestion_button, accusation_button]:
                    button.update(WIN)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if move_button.checkForInput(MENU_MOUSE_POS):
                        moveprompt = font.render('Please select movement', True, (255, 255, 255))
                        WIN.blit(moveprompt, (400 - moveprompt.get_width()/2, 80))
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

