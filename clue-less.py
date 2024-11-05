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
    ##### INITIALIZING VARIABLES #####
    run = True
    active = False
    moveprompt = None
    suggestprompt = None
    accusationprompt = None
    endturnprompt = None
    hasnotsuggested = True
    hasnotaccused = True
    hasnotendedturn = True
    initialdrawing = True
    initiating_game_screen = True
    correctGuess = classes.Guess()
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
    playerlist = []
    playerbuttons = []
    openCards = []
    curr_char = ""
    locations = functions.addLocations()

    while run:
        for event in pygame.event.get():
            ##### QUIT GAME #####
            if event.type == pygame.QUIT:
                run = False
                break
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            ##### HOME SCREEN #####
            if game_state == "home_screen":
                WIN, lobby_button = screens.draw_home_screen()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if lobby_button.checkForInput(MENU_MOUSE_POS):
                        player_x = 200
                        player_y = 400
                        game_state = "lobby"
                        game_over = False

            ##### LOBBY #####
            elif game_state == "lobby":
                WIN, lobby_buttons, player_button, start_button = screens.draw_lobby()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in lobby_buttons:
                        if button.checkForInput(MENU_MOUSE_POS):
                            title = 'Youve selected ' + button.name
                            curr_char = button.name
                    if player_button.checkForInput(MENU_MOUSE_POS):
                        game_players.append(classes.Player(name, curr_char, 0, 0, None))
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

            ##### GAME SCREEN #####
            elif game_state == "game_screen":
                move_button, end_button, suggestion_button, accusation_button = screens.draw_game_screen()
                if initiating_game_screen:
                    playerlist = functions.addCharacters(game_players, WIN)
                    game_players, correctGuess, openCards = functions.dealCards(game_players, correctGuess)
                    initiating_game_screen = False
                for players in playerlist:
                    players.playerbutton.update(WIN)
                for player in playerlist:
                    if player.turn == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if move_button.checkForInput(MENU_MOUSE_POS):
                                moveprompt = font.render('Please select movement', True, (255, 255, 255))
                                suggestprompt = None
                                endgameprompt = None
                                accusationprompt = None
                            if suggestion_button.checkForInput(MENU_MOUSE_POS):
                                suggestprompt = font.render('Please enter suggestion', True, (255, 255, 255))
                                moveprompt = None
                                endgameprompt = None
                                accusationprompt = None
                                hasnotsuggested = True
                            if accusation_button.checkForInput(MENU_MOUSE_POS):
                                accusationprompt = font.render('Please enter accusation', True, (255, 255, 255))
                                moveprompt = None
                                suggestprompt = None
                                endgameprompt = None
                                hasnotaccused = True
                            if end_button.checkForInput(MENU_MOUSE_POS):
                                endturnprompt = font.render('Turn Over!', True, (255, 255, 255))
                                hasnotendedturn = True
                        if moveprompt:
                            WIN.blit(moveprompt, (400 - moveprompt.get_width()/2, 80))
                            possmoves = functions.printMoves(locations, player.playerbutton, WIN)
                            for move in possmoves:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if move.checkForInput(MENU_MOUSE_POS):
                                        player.playerbutton = functions.movePlayer(player.playerbutton,move,WIN)
                                        moveprompt = False
                        if suggestprompt:
                            WIN.blit(suggestprompt, (400 - suggestprompt.get_width()/2, 80))
                            pygame.display.update()
                            if hasnotsuggested:
                                print("Please select room")
                                roominput = input()
                                print("Please select character")
                                charinput = input()
                                print("Please select weapon")
                                weaponinput = input()
                                finalsuggest = 'Player Guessed: ' + roominput + ' ' + charinput + ' ' + weaponinput
                                suggestprompt = font.render(finalsuggest, True, (255, 255, 255))
                                hasnotsuggested = False
                        if accusationprompt:
                            WIN.blit(accusationprompt, (400 - accusationprompt.get_width()/2, 80))
                            pygame.display.update()
                            if hasnotaccused:
                                print("Please select room")
                                roominput = input()
                                print("Please select character")
                                charinput = input()
                                print("Please select weapon")
                                weaponinput = input()
                                if roominput == correctGuess.room and charinput == correctGuess.character and weaponinput == correctGuess.weapon:
                                    finalaccusation = 'Player wins!'
                                else:
                                    finalaccusation = 'Player loses!'
                                accusationprompt = font.render(finalaccusation, True, (255, 255, 255))
                                hasnotaccused = False
                        if endturnprompt:
                            if hasnotendedturn:
                                if playerlist.index(player) < len(playerlist)-1:
                                    playerlist[playerlist.index(player)+1].turn = True
                                else:
                                    playerlist[0].turn = True
                                hasnotendedturn = False
                            endturnprompt = False
                            player.turn = False

            ##### END SCREEN #####
            elif game_state == "end_screen":
                screens.draw_end_screen()
            pygame.display.update()
        clock.tick(120)
    pygame.quit()

if __name__ == "__main__":
    main()

