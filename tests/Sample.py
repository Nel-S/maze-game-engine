from math import ceil, log10, prod
from random import Random
from typing import Literal

import maze_game_engine as mge

DIMENSIONS: Literal[1, 2, 3, 4, 5, 6, 7, 8] = 4 # Number of dimensions the maze expands into. 
MAX_EDGE_LENGTH: int = 3 # Maximum edge length of maze
SEED: int | None = None # (Optional) Seed for the pseudorandom number generators.

prng: Random = Random(SEED)

maze = mge.Maze(DIMENSIONS, (ceil(MAX_EDGE_LENGTH/2), MAX_EDGE_LENGTH), seed=prng.getrandbits(64))
AVAILABLE_MARKS = int(5 * log10(prod(maze.edgeLengths))) # Maximum number of rooms that can be marked simultaneously

player = mge.User("player", maze, markers=AVAILABLE_MARKS, seed=prng.getrandbits(64))
exit = mge.PointOfInterest("exit", maze, seed=prng.getrandbits(64), requireEdge=True)
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