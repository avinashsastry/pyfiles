# A basic demonstration of abstract factory design paradigm
# The aim of thi tutorial is to print a maze, or say a passage with different walls and doors.
# The walls and doors are denoted by different characters, and each type of 
# door and wall will be represented by a set of symbols.

# Our objective is to separate the construction and publishing of the different mazes. 
# In short, the layout of the maze should be independent of the symbol set.

# for simplicity, all symbols will be ASCII characters.

# import abc is required for abstract classes in python
import abc

class Room():
	def __init__(self):
		self.enter = None
		self.leave = None

	def draw(self):
		return "[ ]"

	def printRoom(self):
		rStr = ""
		if self.enter:
			rStr += self.enter.draw()
		rStr += self.draw()
		if self.leave:
			rStr += self.leave.draw()
		return rStr

class CapitalRoom(Room):

	def draw(self):
		return "O"

class SmallRoom(Room):

	def draw(self):
		return "o"

class Door():
	def __init__(self, room1, room2):
		self.room1 = room1
		self.room2 = room2

		room1.leave = self
		room2.enter = self
	
	def draw(self):
		return "="

class CapitalDoor(Door):

	def draw(self):
		return "+"

class SmallDoor(Door):

	def draw(self):
		return "-"

class Maze():
	def __init__(self):
		self.rooms = []

	def addRoom(self, room):
		self.rooms.append(room)

	def printMaze(self):
		mStr = ""
		for r in self.rooms:
			mStr += r.printRoom()
		print mStr

class MazeFactory:
	__metaclass__ = abc.ABCMeta

	def __init__(self):
		pass

	def makeMaze(self):
		m = Maze()
		return m

	@abc.abstractmethod
	def makeRoom(self):
		"""
		Method to create a room
		"""

	@abc.abstractmethod
	def makeDoor(self):
		""" 
		Method to create a door
		"""

class NormalMazeFactory(MazeFactory):
	"""
	Class to create normal mazes
	"""
	def makeRoom(self):
		r = Room()
		return r

	def makeDoor(self, r1, r2):
		d = Door(r1, r2)
		return d

class CapitalMazeFactory(MazeFactory):
	"""
	Class to create 'capital' mazes
	"""
	def makeRoom(self):
		r = CapitalRoom()
		return r

	def makeDoor(self, r1, r2):
		d = CapitalDoor(r1, r2)
		return d

class SmallMazeFactory(MazeFactory):
	"""
	Class to create normal mazes
	"""
	def makeRoom(self):
		r = SmallRoom()
		return r

	def makeDoor(self, r1, r2):
		d = SmallDoor(r1, r2)
		return d

def createMaze(M):
	"""
	M is a maze factory
	"""
	m = M.makeMaze()
	# let's make one with 3 rooms connected by 2 doors

	r1 = M.makeRoom()
	r2 = M.makeRoom()
	r3 = M.makeRoom()

	d1 = M.makeDoor(r1, r2)
	d2 = M.makeDoor(r2, r3)

	m.addRoom(r1)
	m.addRoom(r2)
	m.addRoom(r3)
	
	m.printMaze()

nf = NormalMazeFactory()
sf = SmallMazeFactory()
cf = CapitalMazeFactory()
createMaze(nf)
createMaze(sf)
createMaze(cf)