import os

def start_board(grid, board_size: int):
    for i in range(board_size):
        grid.append([])

    for line in grid:
        for i in range(board_size):
            line.append(None)

def print_board(grid, grid_size):
    linenum = -1
    printTopCoordinates(grid_size)
    for line in grid:
        grid_line = ""
        linenum += 1
        for sqr in line:
            if sqr == None or sqr == 0:
                grid_line += "| ░ |"
            else:
                grid_line += f"| {sqr} |"
        print(grid_line, linenum, "\n")
# A simple function to clear the console.
def clearConsole():
    os.system("cls")

def rangeChar(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

# Fastest way I found to print letters (A-O) coordinates without messing with the grid itself
# This function works by checking grid size and printing the letters in order
# The left coordinates (1-15) are currently being printed inside print_board function
def printTopCoordinates(gridSize):
    for character in rangeChar("A", chr(ord("@") + gridSize)):
        print(f"| {character} |", end="")
    print()
    print()
