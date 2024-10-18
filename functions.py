import classes

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

#def addLocations(locList, locSpot, xCoord, yCoord):
#    for i in range(locSpot):
#        newSpot = classes.Location(locSpot[i],xCoord[i],yCoord[i])
#        locList.append(newSpot)
 #   return locList