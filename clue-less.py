import pygame
from network import Network
import pickle
import time
import random
import screens
import functions
import classes

pygame.init()
pygame.font.init()

global WIDTH, HEIGHT
global WIN
global start_button

def main():
    clock = pygame.time.Clock()
    ##### INITIALIZING VARIABLES #####
    run = True
    active = False
    font = pygame.font.SysFont('comicsans',40)
    prompt = font.render(' ', True, (255, 255, 255))
    hasnotsuggested = True
    hasnotaccused = True
    hasnotendedturn = True
    hasnotchosenmove = True
    displaymoves = False
    initialdrawing = True
    initiating_game_screen = True
    correctGuess = classes.Guess(None, None, None)
    game_state = "home_screen"
    white = pygame.Color('white')
    color_passive = pygame.Color('gray15')
    color_active = pygame.Color('green2')
    color = color_passive
    name = "Type Name"
    globalprompt = " "
    title = 'Please select your character'
    startwait = "Waiting for all players to join"
    waiting = " "
    startinggame = " "
    name_box = pygame.Rect(250,725/2,300,50)
    game_players = []
    playerbuttons = []
    localplayers = []
    playerNames = []
    possmovebuttons = []
    openCards = []
    curr_char = ""

    ##### INITIALIZING THE NETWORK, ASSIGN PLAYER NUMBERS #####
    n = Network()
    onlineplayer = n.getP()
    print("You are player", onlineplayer)
    while run:
        clock.tick(60)
        try:
            game = n.send(["get", None])
        except:
            run = False
            print("Couldn't get game")
            break

        for event in pygame.event.get():
            ##### QUIT GAME #####
            if event.type == pygame.QUIT:
                run = False
                break
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            ##### HOME SCREEN #####
            if game_state == "home_screen":
                WIN, lobby_button = screens.draw_home_screen()
                if waiting != " ":
                    WIN.blit(waiting, (800 / 2 - waiting.get_width() / 2, 625))
                if game.connected():
                    waiting = font.render("All players connected!", 1, (255, 255, 255), True)
                    pygame.display.update()
                if not (game.connected()):
                    waiting = font.render("Waiting for all players", 1, (255, 255, 255), True)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if lobby_button.checkForInput(MENU_MOUSE_POS):
                        if game.connected():
                            player_x = 200
                            player_y = 400
                            game_state = "lobby"
                            game_over = False

            ##### LOBBY #####
            elif game_state == "lobby":
                WIN, lobby_buttons, player_button, start_button = screens.draw_lobby()
                WIN = game.showPlayers(WIN)
                smallfont = pygame.font.SysFont('comicsansms', 30)
                startinggame = smallfont.render(startwait, True, (255, 255, 255))
                WIN.blit(startinggame, (400-startinggame.get_width()/2, 20))
                if len(game.gameplayers) == 3:
                    startwait = "Ready to play!"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in lobby_buttons:
                        if button.checkForInput(MENU_MOUSE_POS):
                            title = 'Youve selected ' + button.name
                            curr_char = button.name
                    if player_button.checkForInput(MENU_MOUSE_POS):
                        game.gameplayers.append(classes.Player(name, curr_char, 0, 0, None))
                        if onlineplayer == 0:
                            game.gameplayers[0].turn = True
                        game = n.send(["add player",game.gameplayers])
                        title = "Player Added!"
                        name = "Type Name"
                    if start_button.checkForInput(MENU_MOUSE_POS):
                        if len(game.gameplayers) == 3:
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
                game.redrawWindow(WIN, game, localplayers)

            ##### GAME SCREEN #####
            elif game_state == "game_screen":
                move_button, end_button, suggestion_button, accusation_button = screens.draw_game_screen()
                game = n.send(["update screen",None])
                font = pygame.font.SysFont('comicsansms', 30)
                WIN = game.showTurn(WIN)
                countp = 0
                for p in localplayers:
                    p.x = game.gameplayers[countp].x
                    p.y = game.gameplayers[countp].y
                    countp += 1
                game.redrawWindow(WIN, game, localplayers)
                if initiating_game_screen:
                    game = n.send(["add players", game.gameplayers])
                    localplayers = game.addCharacters(game.gameplayers, WIN)
                    game = n.send(["verify cards", None])
                    if not game.dealtCards:
                        game.gameplayers, game.correctGuess, openCards = game.dealCards(game.gameplayers, correctGuess)
                        dealtCards = True
                        print('Here is a hint...',correctGuess.weapon, correctGuess.character, correctGuess.room)
                        game = n.send(["dealing cards", dealtCards, openCards, correctGuess, game.gameplayers])
                    initiating_game_screen = False
                if len(openCards) != 0:
                    game.showOpenCards(openCards, WIN)
                for players in localplayers:
                    players.playerbutton.update(WIN)
                game = n.send(["verify screen", None])
                player = game.gameplayers[onlineplayer]
                game.showPlayerCards(player.cards, WIN)
                if player.turn == False:
                    globalprompt = game.globalprompt
                    bigprompt = font.render(globalprompt, True, (255, 255, 255))
                    WIN.blit(bigprompt, (400-bigprompt.get_width()/2, 100))
                if player.turn == True:
                    hasnotchosenmove = True
                    coverbox = pygame.Rect(685,150,115,500)
                    WIN.blit(prompt, (400 - prompt.get_width()/2, 100))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        ### PLAYER CHOOSES TO MOVE THEIR CHARACTER ###
                        if move_button.checkForInput(MENU_MOUSE_POS):
                            hasnotendedturn = True
                            coverbox = pygame.Rect(0,100,800,50)
                            globalprompt = 'Please select movement'
                            prompt = font.render(globalprompt, True, (255, 255, 255))
                            WIN.blit(prompt, (400 - prompt.get_width()/2, 100))
                            pygame.display.update()
                            displaymoves = True
                        ### PLAYER CHOOSES TO MAKE A SUGGESTION ###
                        if suggestion_button.checkForInput(MENU_MOUSE_POS):
                            hasnotendedturn = True
                            coverbox = pygame.Rect(0,100,800,50)
                            globalprompt = 'Please enter suggestion'
                            prompt = font.render(globalprompt, True, (255, 255, 255))
                            WIN.blit(prompt, (400 - prompt.get_width()/2, 100))
                            pygame.display.update()
                            if hasnotsuggested:
                                globalprompt, hasnotsuggested = game.makeSuggestion(player.name)
                                game = n.send(["suggestion",globalprompt])
                                prompt = font.render(' ', True, (255, 255, 255))
                            pygame.display.update()
                        ### PLAYER CHOOSES TO MAKE AN ACCUSATION ###
                        if accusation_button.checkForInput(MENU_MOUSE_POS):
                            hasnotendedturn = True
                            coverbox = pygame.Rect(0,100,800,50)
                            globalprompt = 'Please enter accusation'
                            prompt = font.render(globalprompt, True, (255, 255, 255))
                            WIN.blit(prompt, (400 - prompt.get_width()/2, 80))
                            game.redrawWindow(WIN, game, localplayers)
                            if hasnotaccused:
                                globalprompt, hasnotaccused = game.makeAccusation(correctGuess, player.name)
                            game = n.send(["accusation", globalprompt])
                            prompt = font.render(' ', True, (255, 255, 255))
                        ### PLAYER CHOOSES TO END THEIR TURN ###
                        if end_button.checkForInput(MENU_MOUSE_POS):
                            coverbox = pygame.Rect(0,100,800,50)
                            hasnotaccused = True
                            hasnotsuggested = True
                            if hasnotendedturn:
                                game.gameplayers = game.endTurn(game.gameplayers, player)
                                game = n.send(["end turn", game.gameplayers])
                                hasnotendedturn = False
                    if displaymoves:
                        locations = game.addLocations()
                        possmovebuttons = game.printMoves(locations, localplayers[onlineplayer].playerbutton, WIN)
                        for move in possmovebuttons:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if move.checkForInput(MENU_MOUSE_POS):
                                    localplayers[onlineplayer].playerbutton = game.movePlayer(localplayers[onlineplayer].playerbutton, move, WIN)
                                    game = n.send(["move player", onlineplayer, player])
                                    prompt = font.render(' ', True, (255, 255, 255))
                                    displaymoves = False

            ##### END SCREEN #####
            elif game_state == "end_screen":
                screens.draw_end_screen()
            pygame.display.update()
        clock.tick(120)
    pygame.quit()

if __name__ == "__main__":
    main()