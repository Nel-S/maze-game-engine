import math
import random

maxMazeSize = [3,3,3] #Max maze size in each direction
markKeywords = {True: 'Unmark', False: 'Mark'} #Keywords to mark/unmark rooms
availableMarks = 10 #Max number of rooms that can be marked simultaneously

print('\nGOAL: Find the exit of a maze of unknown size. You may also mark up to', availableMarks, 'rooms at once to help navigate the maze.')
print('Good luck!\n')

def addAdjacentCell(cellCoords, changedCoordinateIndex, change):
    newCellCoords = list(cellCoords)
    newCellCoords[changedCoordinateIndex] += change
    newCellCoords = tuple(newCellCoords)
    if maze[newCellCoords]['Directions']:
        return
    candidates.append(newCellCoords)
    maze[min(cellCoords, newCellCoords)]['Directions'].append(directions[changedCoordinateIndex])
    maze[max(cellCoords, newCellCoords)]['Directions'].append(directions[changedCoordinateIndex + dimension])

lengths = [random.randint(math.ceil(x/2), x) for x in maxMazeSize]
dimension = len(lengths)

maze = {(x, y, z): {'Directions': [], 'Marked': False} for x in range(lengths[0]) for y in range(lengths[1]) for z in range(lengths[2])}
candidates = [tuple([random.randrange(x) for x in lengths])]
directions = ['North', 'East', 'Up', 'South', 'West', 'Down'] #Needs generalization
while len(candidates):
    cellCoords = candidates.pop(random.randrange(len(candidates))) #Both from Python docs
    for x in range(dimension):
        if cellCoords[x] > 0:
            addAdjacentCell(cellCoords, x, -1)
        if cellCoords[x] < lengths[x] - 1:
            addAdjacentCell(cellCoords, x, 1)

currentCoordinates = tuple([random.randrange(x) for x in lengths])
while True:
    sideDimension = random.randrange(dimension)
    endCoordinates = [random.randrange(x) for x in lengths]
    endCoordinates[sideDimension] = random.randint(0,1) * (lengths[sideDimension] - 1)
    endCoordinates = tuple(endCoordinates)
    if endCoordinates != currentCoordinates:
        break

while currentCoordinates != endCoordinates:
    currentDirections = maze[currentCoordinates]['Directions']
    currentMarkedStatus = maze[currentCoordinates]['Marked']
    if currentMarkedStatus:
        print('The room you are in is marked.')
    print('In this room, you can go ', end='', flush=True)
    print(currentDirections[0], end='', flush=True)
    for x in currentDirections[1:-1]:
        print(', ' + x, end='', flush=True)
    if len(currentDirections) > 1:
        print(' or ' + currentDirections[-1], end='', flush=True)
    print('. ', end='', flush=True)
    if currentMarkedStatus or availableMarks:
        print('You can also', markKeywords[currentMarkedStatus], 'this room.', end='', flush=True)
    print('')
    userInput = ''
    while userInput not in currentDirections:
        userInput = str(input('> '))
        if userInput == markKeywords[False]:
            if maze[currentCoordinates]['Marked']:
                print('This room is already marked.')
            elif not availableMarks:
                print('You have already marked', availableMarks, ' marked right now, so you can\'t mark any more at this moment.')
            else:
                maze[currentCoordinates]['Marked'] = True
                availableMarks -= 1
                print('The room you are in has been marked.')
        elif userInput == markKeywords[True]:
            if not maze[currentCoordinates]['Marked']:
                print('This room is already unmarked.')
            else:
                maze[currentCoordinates]['Marked'] = False
                availableMarks += 1
                print('The room you are in has been unmarked.')
    currentCoordinates = list(currentCoordinates)
    for x in range(dimension):
        currentCoordinates[x] += (userInput == directions[x]) - (userInput == directions[x + dimension])
    currentCoordinates = tuple(currentCoordinates)
    print('')
print('You have reached the end of the maze! Congratulations!')
