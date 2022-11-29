from random import randint
import time
from first_test import print_board

# Main module for autoplacement
def shipPlacement(grid, ship, gridSize, auto):
    gridSize = gridSize
    grid = grid
    if ship == "carrier":
        shipSize = 5
        shipTag = "R"
    elif ship == "battleship":
        shipSize = 4
        shipTag = "B"
    elif ship == "cruiser":
        shipSize = 3
        shipTag = "C"
    elif ship == "destroyer":
        shipSize = 2
        shipTag = "D"
    if auto:
        # direction == 0: up, 1: down, 2: left, 3: right
        direction = randint(0, 3)
        shipStart = (randint(0, gridSize - 1), randint(0, gridSize - 1))
        moveDirection, isValid = validDirection(grid, direction, shipSize, shipStart, gridSize)
        while isValid == False:
            direction = randint(0, 3)
            shipStart = (randint(0, gridSize - 1), randint(0, gridSize - 1))
            moveDirection, isValid = validDirection(grid, direction, shipSize, shipStart, gridSize)
    else:
        direction, isValid, shipStart = manualInput(grid, shipSize, gridSize, ship)
        while len(shipStart) < 1:
            print("Valores inválidos!")
            time.sleep(2)
            print_board(grid, gridSize)
            direction, isValid, shipStart = manualInput(grid, shipSize, gridSize, ship)
    shipDeployment(grid, shipSize, shipTag, shipStart, direction)
    print_board(grid, gridSize)
    time.sleep(2)

    # A specific function to receive player input during placement
def manualInput(grid, shipSize, gridSize, ship):
    isValid = False
    try:
        shipPosition = input("Digite as coordenadas de início e direção do navio"
                    f" Ex: A0 2 ou A0 3\n0 - Para cima || 1 - Para baixo || 2 - Para a esquerda || 3 - Para a direita\n"
                    f"Navio atual: {ship}\nTamanho: {shipSize}\n").lower().split()
        shipLetter = ord(shipPosition[0][0]) - ord("a")
        direction, isValid = validDirection(grid, int(shipPosition[1][0]), shipSize, (int(shipPosition[0][1]), shipLetter), gridSize)
        if isValid == True:
            return [direction, isValid, (int(shipPosition[0][1]), shipLetter)]
        else:
            return [direction, isValid, ()]
    except:
        return [direction, isValid, ()]

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