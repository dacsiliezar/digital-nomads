from re import X


class Player:
	def __init__(self, name, character, x, y, playerbutton):
		self.name = name
		self.character = character
		self.x = x
		self.y = y
		self.playerbutton = playerbutton
		self.turn = False
		self.cards = []

class Guess:
    weapon = ""
    room = ""
    character = ""

class Location():
	def __init__(self, loc, x, y):
		self.loc = loc
		self.x = x
		self.y = y

class ImageButton():
	def __init__(self, image, pos, name):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.name = name
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

class CharacterStarts():
	def __init__(self, character, x, y):
		self.character = character
		self.x = x
		self.y = y

weapons = ["Candlestick", "Wrench", "Lead Pipe", "Rope", "Dagger", "Revolver"]
characters = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White"]
characterX = [483,220,572,218,295,504]
characterY = [214,258,306,495,554,547]
secret_passages = ["Study-Kitchen","Lounge-Conservatory"]