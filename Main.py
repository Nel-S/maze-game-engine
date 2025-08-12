from math import ceil, log10, prod
from random import Random

from Maze import Maze
from MazeObjects.User import User
from MazeObjects.PointOfInterest import PointOfInterest
from Settings import *

prng: Random = Random(SEED)

maze = Maze(DIMENSIONS, (ceil(MAX_EDGE_LENGTH/2), MAX_EDGE_LENGTH), seed=prng.getrandbits(64))
AVAILABLE_MARKS = int(5 * log10(prod(maze.edgeLengths))) # Maximum number of rooms that can be marked simultaneously

player = User("player", maze, markers=AVAILABLE_MARKS, seed=prng.getrandbits(64))
exit = PointOfInterest("exit", maze, seed=prng.getrandbits(64), requireEdge=True)
while player.location == exit.location: player.placeRandomly()

# Prints instructions
print(f"""Welcome to this Python maze game!
	  
GOAL: Find the exit of a maze of unknown size. You may also mark up to {AVAILABLE_MARKS} rooms at once to help navigate the maze.
Good luck!
""")

try:
	while player.location != exit.location: player.move()
	print("You have reached the end of the maze! Congratulations!") # Prints victory message
except KeyboardInterrupt:
	pass