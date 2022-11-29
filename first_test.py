import cpuModule

grid_cpu = []
grid_player = []
grid_size = 10

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def start_board(grid, board_size: int):
    for i in range(board_size):
        grid.append([])

    for line in grid:
        for i in range(board_size):
            line.append(None)

# Fastest way I found to print letters (A-O) coordinates without messing with the grid itself
# This function works by checking grid size and printing the letters in order
# The left coordinates (1-15) are currently being printed inside print_board function
def printTopCoordinates(grid_size):
    if grid_size == 15:
        for character in range_char("A", "O"):
            if character != "A":
                print(f"| {character} |", end="")
            else:
                print("    A |", end="")
        print()
        print()
    if grid_size == 10:
        for character in range_char("A", "J"):
            if character != "A":
                print(f"| {character} |", end="")
            else:
                print("    A |", end="")
        print()
        print()
    if grid_size == 5:
        for character in range_char("A", "E"):
            if character != "A":
                print(f"| {character} |", end="")
            else:
                print("    A |", end="")
        print()
        print()
                                

def print_board(grid, grid_size):
    linenum = -1
    printTopCoordinates(grid_size)
    for line in grid:
        grid_line = ""
        linenum += 1
        for sqr in line:
            if sqr == None:
                grid_line += "| ░ |"
            else:
                grid_line += f"| {sqr} |"
        print(linenum, grid_line, "\n")

if __name__ == "__main__":
    start_board(grid_player, grid_size)
    cpuModule.shipPlacement(grid_player, "destroyer", grid_size)
    cpuModule.shipPlacement(grid_player, "destroyer", grid_size)
    cpuModule.shipPlacement(grid_player, "battleship", grid_size)
    cpuModule.shipPlacement(grid_player, "cruiser", grid_size)
    cpuModule.shipPlacement(grid_player, "carrier", grid_size)
    print_board(grid_player, grid_size)