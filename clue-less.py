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
    font = pygame.font.SysFont('comicsansms',40)
    prompt = font.render(' ', True, (255, 255, 255))
    hasnotsuggested = True
    hasnotaccused = True
    hasnotendedturn = True
    hasnotchosenmove = True
    displaymoves = False
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
    name_box = pygame.Rect(250,725/2,300,50)
    game_players = []
    playerbuttons = []
    possmovebuttons = []
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
                    game_players = functions.addCharacters(game_players, WIN)
                    game_players, correctGuess, openCards = functions.dealCards(game_players, correctGuess)
                    initiating_game_screen = False
                if len(openCards) != 0:
                    functions.showOpenCards(openCards, WIN)
                for players in game_players:
                    players.playerbutton.update(WIN)
                for player in game_players:
                    if player.turn == True:
                        hasnotchosenmove = True
                        coverbox = pygame.Rect(685,150,115,500)
                        functions.showPlayerCards(player.cards, WIN)
                        WIN.blit(prompt, (400 - prompt.get_width()/2, 80))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            ### PLAY CHOOSES TO MOVE THEIR CHARACTER ###
                            if move_button.checkForInput(MENU_MOUSE_POS):
                                hasnotendedturn = True
                                coverbox = pygame.Rect(0,80,800,50)
                                prompt = font.render('Please select movement', True, (255, 255, 255))
                                WIN.blit(prompt, (400 - prompt.get_width()/2, 80))
                                pygame.display.update()
                                displaymoves = True
                            ### PLAYER CHOOSES TO MAKE A SUGGESTION ###
                            if suggestion_button.checkForInput(MENU_MOUSE_POS):
                                hasnotendedturn = True
                                coverbox = pygame.Rect(0,80,800,50)
                                prompt = font.render('Please enter suggestion', True, (255, 255, 255))
                                WIN.blit(prompt, (400 - prompt.get_width()/2, 80))
                                pygame.display.update()
                                if hasnotsuggested:
                                    prompt, hasnotsuggested = functions.makeSuggestion()
                                pygame.display.update()
                            ### PLAYER CHOOSES TO MAKE AN ACCUSATION ###
                            if accusation_button.checkForInput(MENU_MOUSE_POS):
                                hasnotendedturn = True
                                coverbox = pygame.Rect(0,80,800,50)
                                prompt = font.render('Please enter accusation', True, (255, 255, 255))
                                WIN.blit(prompt, (400 - prompt.get_width()/2, 80))
                                pygame.display.update()
                                if hasnotaccused:
                                    prompt, hasnotaccused = functions.makeAccusation(correctGuess)
                                pygame.display.update()
                            ### PLAYER CHOOSES TO END THEIR TURN ###
                            if end_button.checkForInput(MENU_MOUSE_POS):
                                coverbox = pygame.Rect(0,80,800,50)
                                prompt = font.render('Turn Over!', True, (255, 255, 255))
                                hasnotaccused = True
                                hasnotsuggested = True
                                if hasnotendedturn:
                                    game_players = functions.endTurn(game_players, player)
                                    hasnotendedturn = False
                        if displaymoves:
                            possmovebuttons = functions.printMoves(locations, player.playerbutton, WIN)
                            for move in possmovebuttons:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if move.checkForInput(MENU_MOUSE_POS):
                                        player.playerbutton = functions.movePlayer(player.playerbutton, move, WIN)
                                        displaymoves = False

            ##### END SCREEN #####
            elif game_state == "end_screen":
                screens.draw_end_screen()
            pygame.display.update()
        clock.tick(120)
    pygame.quit()

if __name__ == "__main__":
    main()

