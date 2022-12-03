import time
from random import randint
from boardModule import print_board
from boardModule import clearConsole

# Main module for ship placement. 
# Auto should be True for autoplacement and False for manual input.
def shipPlacement(grid, ship, auto):
    grid = grid
    shipSize, shipTag = getShipId(ship)
    if auto:
        # direction == 0: up, 1: down, 2: left, 3: right
        direction = randint(0, 3)
        shipStart = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
        moveDirection, isValid = checkValidDirection(grid, direction, shipSize, shipStart)
        while isValid == False:
            direction = randint(0, 3)
            shipStart = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
            moveDirection, isValid = checkValidDirection(grid, direction, shipSize, shipStart)
    else:
        direction, isValid, shipStart = doManualInput(grid, shipSize, ship)
        while len(shipStart) < 1:
            direction, isValid, shipStart = doManualInput(grid, shipSize, ship)
    deployShip(grid, shipSize, shipTag, shipStart, direction)
    clearConsole()
    print_board(grid, len(grid))
    if auto: print("\n\nCPU is placing its ships...")
    time.sleep(1)

#Simple function to identify ships being currently placed
def getShipId(ship):
    if ship == "carrier":
        return [5, "R"]
    elif ship == "battleship":
        return [4, "B"]
    elif ship == "cruiser":
        return [3, "C"]
    elif ship == "destroyer":
        return [2, "D"]

# A specific function to receive player input during placement
def doManualInput(grid, shipSize, ship):
    isValid = False
    try:
        shipPosition = input("Type ship coordinates and ship direction"
                    f" E.g.: A0 2 or A0 3\n0 - Up || 1 - Down || 2 - Left || 3 - Right\n"
                    f"Navio atual: {ship}\nTamanho: {shipSize}\n").lower().split()
        shipLetter = ord(shipPosition[0][0]) - ord("a")
        direction, isValid = checkValidDirection(grid, int(shipPosition[1][0]), shipSize, (int(shipPosition[0][1]), shipLetter))
        if isValid == True:
            return [direction, isValid, (int(shipPosition[0][1]), shipLetter)]
        else:
            return handleInputException(grid)
    except:
        return handleInputException(grid)

# This function analyses grid availability in the desired direction without actually deploying units
# The loops for shipAdjacent list are supposed to check for collision so no ship may be "glued" to each other
def checkValidDirection(grid, direction, shipSize, shipStart):
    shipPosition = []
    if direction == 0:
        if shipStart[0] - shipSize >= 0:
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0] - x][shipStart[1]])
            if shipPosition.count(None) == shipSize and shipPosition.count(0) == 0:
                return [direction, True]
    elif direction == 1:
        if shipStart[0] + shipSize <= len(grid):
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0] + x][shipStart[1]])
            if shipPosition.count(None) == shipSize and shipPosition.count(0) == 0:
                return [direction, True]
    elif direction == 2:
        if shipStart[1] - shipSize >= 0:
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0]][shipStart[1] - x])
            if shipPosition.count(None) == shipSize and shipPosition.count(0) == 0:
                return [direction, True]
    elif direction == 3:
        if shipStart[1] + shipSize <= len(grid):
            for x in range(shipSize):
                shipPosition.append(grid[shipStart[0]][shipStart[1] + x])
            if shipPosition.count(None) == shipSize and shipPosition.count(0) == 0:
                return [direction, True]
    return [direction, False]

# This function deploy units after confirming there are enough empty slots
def deployShip(grid, shipSize, shipTag, shipStart, moveDirection):
    if moveDirection == 0:
        for i in range(shipSize):
            grid[shipStart[0] - i][shipStart[1]] = shipTag
            createCollisionBlock(grid, shipStart[0] - i, shipStart[1])
    elif moveDirection == 1:
        for i in range(shipSize):
            grid[shipStart[0] + i][shipStart[1]] = shipTag
            createCollisionBlock(grid, shipStart[0] + i, shipStart[1])
    elif moveDirection == 2:
        for i in range(shipSize):
            grid[shipStart[0]][shipStart[1] - i] = shipTag
            createCollisionBlock(grid, shipStart[0], shipStart[1] - i)
    elif moveDirection == 3:
        for i in range(shipSize):
            grid[shipStart[0]][shipStart[1] + i] = shipTag
            createCollisionBlock(grid, shipStart[0], shipStart[1] + i)
    createCollisionBlock(grid, shipStart[0], shipStart[1])

#This function will create a collision block around each ship block when possible
def createCollisionBlock(grid, axisY, axisX):
    if axisY + 1 < len(grid) and (grid[axisY + 1][axisX] == None or grid[axisY + 1][axisX] == 0):
        grid[axisY + 1][axisX] = 0
    if axisX + 1 < len(grid) and (grid[axisY][axisX + 1] == None or grid[axisY][axisX + 1] == 0):
        grid[axisY][axisX + 1] = 0
    if axisX - 1 >= 0 and (grid[axisY][axisX - 1] == None or grid[axisY][axisX - 1] == 0):
        grid[axisY][axisX - 1] = 0
    if axisY - 1 >= 0 and (grid[axisY - 1][axisX] == None or grid[axisY - 1][axisX] == 0):
        grid[axisY - 1][axisX] = 0

# A simple function to handle any input error while placing ships
def handleInputException(grid):
    print("Invalid values!")
    time.sleep(2)
    clearConsole()
    print_board(grid, len(grid))
    return [0, False, ()]