import classes
import pygame
import random

##### INITIAL FUNCTION TO GO FROM ENTRY SCREEN INTO LOBBY #####
def joinGame():
    print("Welcome to Clue-Less! Please choose your character")

##### PRINTS ALL PLAYERS TO TERMINAL SO YOU CAN SEE ALL THEIR DATA #####
def printPlayers(players_list):
    for i in players_list:
        print(vars(i))

##### WHEN PLAYER SELECTS OPTION TO MAKE A SUGGESTION #####
def makeSuggestion(guess: classes.Guess, player: classes.Player):
    print(player.name, " has made a suggestion:")
    print(vars(guess))

##### WHEN PLAYER SELECTS OPTION TO MAKE AN ACCUSATION #####
def makeAccusation(guess: classes.Guess, player: classes.Player, correct_guess: classes.Guess):
    print(player.name, " has accused:")
    print(vars(guess))
    if (guess.character == correct_guess.character and guess.room == correct_guess.room and guess.weapon == correct_guess.weapon):
        print(player.name, " wins!")
    else:
        print("Incorrect! The game is over. The correct answer was:")
        print(vars(correct_guess))

##### ADDS ALL POSSIBLE LOCATIONS INTO A LIST #####
def addLocations():
    data = []
    rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
    roomX = [218,398,579,223,391,574,212,398,590]
    roomY = [204,236,226,325,360,392,571,537,550]
    hallways = [1,2,3,4,5,6,7,8,9,10,11,12]
    hallX = [314,483,220,396,572,315,463,218,394,579,295,504]
    hallY = [214,214,258,306,306,355,379,495,463,478,554,547]
    counter = 0
    for i in rooms:
      newdata = classes.Location(i,roomX[counter],roomY[counter])
      data.append(newdata)
      counter = counter + 1
    for i in hallways:
      newdata = classes.Location(i,hallX[i-1],hallY[i-1])
      data.append(newdata)
    return data

##### ADDS CHARACTERS THAT HAVE BEEN SELECTED INTO THE GAME #####
def addCharacters(gameplayers, WIN):
    characterList = []
    characterbuttons = []
    characters = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
    characterX = [483,220,572,218,295,504]
    characterY = [214,258,306,495,554,547]
    scarlet_button = classes.ImageButton(image=pygame.image.load("images/scar_button.png"), pos=(483,214), name="Miss Scarlet")
    colonel_button = classes.ImageButton(image=pygame.image.load("images/mustard_button.png"), pos=(220,258), name="Colonel Mustard")
    green_button = classes.ImageButton(image=pygame.image.load("images/green_button.png"), pos=(572,306), name="Mr. Green")
    peacock_button = classes.ImageButton(image=pygame.image.load("images/peacock_button.png"), pos=(218, 495), name="Mrs. Peacock")
    white_button = classes.ImageButton(image=pygame.image.load("images/white_button.png"), pos=(295, 554), name="Mrs. White")
    plum_button = classes.ImageButton(image=pygame.image.load("images/plum_button.png"), pos=(504,547), name="Professor Plum")

    for char in gameplayers:
        counter = 0
        for charlist in characters:
            if char.character == charlist:
                newchar = classes.Player(char.name, char.character,characterX[counter],characterY[counter], None)
                if newchar.character == "Miss Scarlet":
                    newchar.turn = True
                for button in [scarlet_button, colonel_button, green_button, peacock_button, white_button, plum_button]:
                    if button.name == newchar.character:
                        newchar.playerbutton = button
                        newchar.playerbutton.update(WIN)
                characterList.append(newchar)
            counter = counter + 1
    return characterList

##### SHOWS POSSIBLE OPTIONS FOR MOVEMENT WHEN PLAYER CHOOSES TO MOVE #####
def printMoves(locations, playerbutton, WIN):
    possmoves = []
    possmovebuttons = []
    for move in locations:
        if move.x == playerbutton.x_pos and move.y == playerbutton.y_pos:
            if move.loc == "Study":
                for validmove in locations:
                    if validmove.loc == 1 or validmove.loc == 3:
                        possmoves.append(validmove)
            if move.loc == "Hall":
                for validmove in locations:
                    if validmove.loc == 1 or validmove.loc == 2 or validmove.loc == 4:
                        possmoves.append(validmove)
            if move.loc == "Lounge":
                for validmove in locations:
                    if validmove.loc == 2 or validmove.loc == 5:
                        possmoves.append(validmove)
            if move.loc == "Library":
                for validmove in locations:
                    if validmove.loc == 3 or validmove.loc == 6 or validmove.loc == 8:
                        possmoves.append(validmove)
            if move.loc == "Billiard Room":
                for validmove in locations:
                    if validmove.loc == 4 or validmove.loc == 6 or validmove.loc == 7 or validmove.loc == 9:
                        possmoves.append(validmove)
            if move.loc == "Dining Room":
                for validmove in locations:
                    if validmove.loc == 5 or validmove.loc == 7 or validmove.loc == 10:
                        possmoves.append(validmove)
            if move.loc == "Conservatory":
                for validmove in locations:
                    if validmove.loc == 8 or validmove.loc == 11:
                        possmoves.append(validmove)
            if move.loc == "Ballroom":
                for validmove in locations:
                    if validmove.loc == 9 or validmove.loc == 11 or validmove.loc == 12:
                        possmoves.append(validmove)
            if move.loc == "Kitchen":
                for validmove in locations:
                    if validmove.loc == 10 or validmove.loc == 12:
                        possmoves.append(validmove)
            if move.loc == 1:
                for validmove in locations:
                    if validmove.loc == "Study" or validmove.loc == "Hall":
                        possmoves.append(validmove)
            if move.loc == 2:
                for validmove in locations:
                    if validmove.loc == "Hall" or validmove.loc == "Lounge":
                        possmoves.append(validmove)
            if move.loc == 3:
                for validmove in locations:
                    if validmove.loc == "Study" or validmove.loc == "Library":
                        possmoves.append(validmove)
            if move.loc == 4:
                for validmove in locations:
                    if validmove.loc == "Hall" or validmove.loc == "Billiard Room":
                        possmoves.append(validmove)
            if move.loc == 5:
                for validmove in locations:
                    if validmove.loc == "Lounge" or validmove.loc == "Dining Room":
                        possmoves.append(validmove)
            if move.loc == 6:
                for validmove in locations:
                    if validmove.loc == "Billiard Room" or validmove.loc == "Library":
                        possmoves.append(validmove)
            if move.loc == 7:
                for validmove in locations:
                    if validmove.loc == "Dining Room" or validmove.loc == "Billiard Room":
                        possmoves.append(validmove)
            if move.loc == 8:
                for validmove in locations:
                    if validmove.loc == "Library" or validmove.loc == "Conservatory":
                        possmoves.append(validmove)
            if move.loc == 9:
                for validmove in locations:
                    if validmove.loc == "Billiard Room" or validmove.loc == "Ballroom":
                        possmoves.append(validmove)
            if move.loc == 10:
                for validmove in locations:
                    if validmove.loc == "Dining Room" or validmove.loc == "Kitchen":
                        possmoves.append(validmove)
            if move.loc == 11:
                for validmove in locations:
                    if validmove.loc == "Conservatory" or validmove.loc == "Ballroom":
                        possmoves.append(validmove)
            if move.loc == 12:
                for validmove in locations:
                    if validmove.loc == "Ballroom" or validmove.loc == "Kitchen":
                        possmoves.append(validmove)
    for move in possmoves:
        move_button = classes.ImageButton(image=pygame.image.load("images/move_button.png"), pos=(move.x,move.y), name="move button")
        move_button.update(WIN)
        possmovebuttons.append(move_button)
    return possmovebuttons

##### UPDATES PLAYER POSITION IF THEY CHOOSE ACCEPTABLE MOVEMENT #####
def movePlayer(playerbutton, move, WIN):
    updated_playerbutton = classes.ImageButton(image=playerbutton.image, pos=(move.x_pos,move.y_pos), name=playerbutton.name)
    playerbutton.update(WIN)
    return updated_playerbutton

##### DEALS ALL CARDS AND GENERATES CORRECT GUESS WHEN GAME IS STARTED #####
def dealCards(gameplayers, correctGuess: classes.Guess):
    rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
    characters = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
    weapons = ["Candlestick", "Wrench", "Lead Pipe", "Rope", "Dagger", "Revolver"]
    correctGuess.room = random.choice(rooms)
    correctGuess.character = random.choice(characters)
    correctGuess.weapon = random.choice(weapons)
    remainingCards = rooms + characters + weapons
    remainingCards.remove(correctGuess.room)
    remainingCards.remove(correctGuess.character)
    remainingCards.remove(correctGuess.weapon)
    openCards = random.sample(remainingCards,(len(remainingCards)%len(gameplayers)))
    for card in openCards:
        remainingCards.remove(card)
    numcards = int(len(remainingCards)/len(gameplayers))
    for j in range(len(gameplayers)):
        for i in range(numcards):
            randomcard = random.choice(remainingCards)
            remainingCards.remove(randomcard)
            gameplayers[j].cards.append(randomcard)
    return gameplayers, correctGuess, openCards