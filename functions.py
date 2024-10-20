import classes
import pygame

def joinGame():
    print("Welcome to Clue-Less! Please choose your character")

def printPlayers(players_list):
    for i in players_list:
        print(vars(i))

def makeSuggestion(guess: classes.Guess, player: classes.Player):
    print(player.name, " has made a suggestion:")
    print(vars(guess))

def makeAccusation(guess: classes.Guess, player: classes.Player, correct_guess: classes.Guess):
    print(player.name, " has accused:")
    print(vars(guess))
    if (guess.character == correct_guess.character and guess.room == correct_guess.room and guess.weapon == correct_guess.weapon):
        print(player.name, " wins!")
    else:
        print("Incorrect! The game is over. The correct answer was:")
        print(vars(correct_guess))

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

def addCharacters(gameplayers, WIN):
    characterList = []
    characters = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White"]
    characterX = [483,220,572,218,295,504]
    characterY = [214,258,306,495,554,547]
    for char in gameplayers:
        counter = 0
        for charlist in characters:
            if char.character == charlist:
                newchar = classes.CharacterStarts(char.character,characterX[counter],characterY[counter])
                characterList.append(newchar)
            counter = counter + 1
    return characterList
def printMoves(locations, WIN):
    for move in locations:
        color = pygame.Color('green2')
        loc_box = pygame.Rect(move.x-25,move.y-25,50,50)
        pygame.draw.rect(WIN,color,loc_box,3)