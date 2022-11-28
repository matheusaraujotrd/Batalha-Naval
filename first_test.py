from random import randint
grid_cpu = []
grid_player = []
grid_size = 10
def start_board(grid, board_size: int):
    for i in range(board_size):
        grid.append([])

    for line in grid:
        for i in range(board_size):
            line.append(None)

def carrier_placement(grid):
    # carrier = 1
    carrier_size = 5
    carrier_placed = False
    while not carrier_placed:
        carrier_start = (randint(0, grid_size - 1), randint(0, grid_size - 1))
        direction = randint(0, 3)
        # 0: up, 1: down, 2: left, 3: right
        if direction == 0:
            if carrier_start[0] - carrier_size >= 0:
                carrier_slots = [grid[carrier_start[0]][carrier_start[1]],
                grid[carrier_start[0] - 1][carrier_start[1]],
                grid[carrier_start[0] - 2][carrier_start[1]],
                grid[carrier_start[0] - 3][carrier_start[1]],
                grid[carrier_start[0] - 4][carrier_start[1]]]
                if carrier_slots.count(None) == carrier_size:
                    for i in range (carrier_size):
                        grid[carrier_start[0] - i][carrier_start[1]] = 1
                    carrier_placed = True
        
        elif direction == 1:
            if carrier_start[0] + carrier_size <= grid_size:
                carrier_slots = [grid[carrier_start[0]][carrier_start[1]],
                grid[carrier_start[0] + 1][carrier_start[1]],
                grid[carrier_start[0] + 2][carrier_start[1]],
                grid[carrier_start[0] + 3][carrier_start[1]],
                grid[carrier_start[0] + 4][carrier_start[1]]]
                if carrier_slots.count(None) == carrier_size:
                    for i in range (carrier_size):
                        grid[carrier_start[0] + i][carrier_start[1]] = 1
                    carrier_placed = True

        elif direction == 2:
            if carrier_start[1] - carrier_size >= 0:
                carrier_slots = [grid[carrier_start[0]][carrier_start[1]],
                grid[carrier_start[0]][carrier_start[1] - 1],
                grid[carrier_start[0]][carrier_start[1] - 2],
                grid[carrier_start[0]][carrier_start[1] - 3],
                grid[carrier_start[0]][carrier_start[1] - 4]]
                if carrier_slots.count(None) == carrier_size:
                    for i in range (carrier_size):
                        grid[carrier_start[0]][carrier_start[1] - i] = 1
                    carrier_placed = True    
        elif direction == 3:
            if carrier_start[1] + carrier_size <= grid_size:
                carrier_slots = [grid[carrier_start[0]][carrier_start[1]],
                grid[carrier_start[0]][carrier_start[1] + 1],
                grid[carrier_start[0]][carrier_start[1] + 2],
                grid[carrier_start[0]][carrier_start[1] + 3],
                grid[carrier_start[0]][carrier_start[1] + 4]]
                if carrier_slots.count(None) == carrier_size:
                    for i in range (carrier_size):
                        grid[carrier_start[0]][carrier_start[1] + i] = 1
                    carrier_placed = True
        
                                

def print_board(grid):

    for line in grid:
        grid_line = ""
        for sqr in line:
            if sqr == None:
                grid_line += "| ░ |"
            else:
                grid_line += f"| █ |"
        print(grid_line, "\n")

start_board(grid_player, grid_size)
print_board(grid_player)