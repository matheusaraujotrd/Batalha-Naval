from random import randint

# Main module for autoplacement
def shipPlacement(grid, ship, gridSize):
    gridSize = gridSize
    grid = grid
    shipPosition = []
    if ship == "carrier":
        shipSize = 5
        shipTag = 4
    elif ship == "battleship":
        shipSize = 4
        shipTag = 3
    elif ship == "cruiser":
        shipSize = 3
        shipTag = 2
    elif ship == "destroyer":
        shipSize = 2
        shipTag = 1

    # direction == 0: up, 1: down, 2: left, 3: right
    direction = randint(0, 3)
    shipStart = (randint(0, gridSize - 1), randint(0, gridSize - 1))
    moveDirection, isValid = validDirection(grid, direction, shipSize, shipStart, gridSize)
    while isValid == False:
        direction = randint(0, 3)
        shipStart = (randint(0, gridSize - 1), randint(0, gridSize - 1))
        moveDirection, isValid = validDirection(grid, direction, shipSize, shipStart, gridSize)
    shipDeployment(grid, shipSize, shipTag, shipStart, moveDirection)

# This function analyses grid availability in the desired direction without actually deploying units
def validDirection(grid, direction, shipSize, shipStart, gridSize):
    shipPosition = []
    if direction == 0:
        if shipStart[0] - shipSize >= 0:
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0] - x][shipStart[1]])
                if shipPosition.count(None) == shipSize:
                    return [direction, True]
    elif direction == 1:
        if shipStart[0] + shipSize <= gridSize:
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0] + x][shipStart[1]])
                if shipPosition.count(None) == shipSize:
                    return [direction, True]
    elif direction == 2:
        if shipStart[1] - shipSize >= 0:
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0]][shipStart[1] - x])
                if shipPosition.count(None) == shipSize:
                    return [direction, True]
    elif direction == 3:
        if shipStart[1] + shipSize <= gridSize:
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0]][shipStart[1] + x])
                if shipPosition.count(None) == shipSize:
                    return [direction, True]
    return [direction, False]

# This function deploy units after confirming there are enough empty slots
def shipDeployment(grid, shipSize, shipTag, shipStart, moveDirection):
    if moveDirection == 0:
        for i in range(shipSize):
            grid[shipStart[0] - i][shipStart[1]] = shipTag
    elif moveDirection == 1:
        for i in range(shipSize):
            grid[shipStart[0] + i][shipStart[1]] = shipTag
    elif moveDirection == 2:
        for i in range(shipSize):
            grid[shipStart[0]][shipStart[1] - i] = shipTag
    elif moveDirection == 3:
        for i in range(shipSize):
            grid[shipStart[0]][shipStart[1] + i] = shipTag