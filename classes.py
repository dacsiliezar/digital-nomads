class Player:
	def __init__(self, name, character):
		self.name = name
		self.character = character
		self.turn = False

class Guess:
    weapon = ""
    room = ""
    character = ""

#class Location():
 #   rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
  #  roomX = [218,398,579,223,391,574,212,398,590]
   # roomY = [204,236,226,325,360,392,571,537,550]

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


weapons = ["Candlestick", "Wrench", "Lead Pipe", "Rope", "Dagger", "Revolver"]
hallways = [1,2,3,4,5,6,7,8,9,10,11,12]
#hallX = 
#hallY = 
characters = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White"]

secret_passages = ["Study-Kitchen","Lounge-Conservatory"]