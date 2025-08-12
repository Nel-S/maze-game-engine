from typing import Literal

DIMENSIONS: Literal[1, 2, 3, 4, 5, 6, 7, 8] = 4 # Number of dimensions the maze expands into. 
MAX_EDGE_LENGTH: int = 3 # Maximum edge length of maze
SEED: int | None = None # (Optional) Seed for the pseudorandom number generators.