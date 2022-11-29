import cpuModule

grid_cpu = []
grid_player = []
grid_size = 10
def start_board(grid, board_size: int):
    for i in range(board_size):
        grid.append([])

    for line in grid:
        for i in range(board_size):
            line.append(None)
        
                                

def print_board(grid):

    for line in grid:
        grid_line = ""
        for sqr in line:
            if sqr == None:
                grid_line += "| ░ |"
            else:
                grid_line += f"| {sqr} |"
        print(grid_line, "\n")

start_board(grid_player, grid_size)
cpuModule.shipPlacement(grid_player, "carrier", grid_size)
cpuModule.shipPlacement(grid_player, "battleship", grid_size)
cpuModule.shipPlacement(grid_player, "cruiser", grid_size)
cpuModule.shipPlacement(grid_player, "destroyer", grid_size)
cpuModule.shipPlacement(grid_player, "destroyer", grid_size)
cpuModule.shipPlacement(grid_player, "destroyer", grid_size)
cpuModule.shipPlacement(grid_player, "battleship", grid_size)
print_board(grid_player)