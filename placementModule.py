import time
from random import randint
from boardModule import print_board, print_board_open
from boardModule import clear_console

# direction variable is used several times in this file. 
## direction == 0: up, 1: down, 2: left, 3: right

# Main module for ship placement. 
# Auto should be True for autoplacement and False for manual input.
def ship_placement(grid, ship, auto):
    grid = grid
    ship_size, ship_tag = get_ship_id(ship)
    if auto:
        direction, ship_start = auto_ship_placement(grid, ship_size)
    else:
        direction, ship_start = do_manual_input(grid, ship_size, ship)
        while len(ship_start) < 1:
            direction, ship_start = do_manual_input(grid, ship_size, ship)
    deploy_ship(grid, ship_size, ship_tag, ship_start, direction)
    clear_console()
    if auto: 
        print("\n\nCPU is placing its ships...")
        print_board(grid, len(grid))
    else:
        print_board_open(grid, len(grid))
    time.sleep(1)

# This function is used for autoplacement.
def auto_ship_placement(grid, ship_size):
    direction = randint(0, 3)
    ship_start = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
    move_direction, is_valid = check_valid_direction(grid, direction, ship_size, ship_start)
    while is_valid == False:
        direction = randint(0, 3)
        ship_start = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
        move_direction, is_valid = check_valid_direction(grid, direction, ship_size, ship_start)
    return [direction, ship_start]

# Simple function to identify ships being currently placed
def get_ship_id(ship: str):
    if ship == "carrier":
        return (5, "R")
    elif ship == "battleship":
        return (4, "B")
    elif ship == "cruiser":
        return (3, "C")
    elif ship == "destroyer":
        return (2, "D")

#Get ship shot id is used to return the name of the ship hit during the game. 
#Get ship shot size may be used to get the size of a ship during a game.
def get_ship_shot_id(ship_list):
    if ship_list == "R":
        return "Carrier"
    elif ship_list == "B":
        return "Battleship"
    elif ship_list == "C":
        return "Cruiser"
    elif ship_list == "D":
        return "Destroyer"
def get_ship_shot_size(ship_list):
    if ship_list == "Carrier":
        return 5
    elif ship_list == "Battleship":
        return 4
    elif ship_list == "Cruiser":
        return 3
    elif ship_list == "Destroyer":
        return 2

# Simple functions to get a specific coordinate in user input
# Both arguments must be STRING type. 
# e.g.: if user inputs D4 as coordinate, you may call get_column_coordinates(input) 
# to reach column D and get_row_coordinates(input) to reach row 4
def get_column_coordinates(player_input):
    if len(player_input[0]) > 1 and len(player_input[0]) < 4:
        return ord(player_input[0][0]) - ord("a")
def get_row_coordinates(player_input):
    if len(player_input[0]) < 3:
        return int(player_input[0][1])
    elif len(player_input[0]) >= 3:
        return (int(player_input[0][1]) * 10) + int(player_input[0][2])


# Get column/rows and get shot column/rows works almost the same, 
# but the above code should be used for placement, 
# while code below is for use during gameloop only.
def get_column_shot_coordinates(player_input):
    if len(player_input) > 1 and len(player_input) < 4:
        return ord(player_input[0]) - ord("a")
def get_row_shot_coordinates(player_input):
    if len(player_input) < 3:
        return int(player_input[1])
    elif len(player_input) >= 3:
        return (int(player_input[1]) * 10) + int(player_input[2])

# A specific function to receive player input during placement
def do_manual_input(grid, ship_size, ship):
    is_valid = False
    try:
        ship_position = input("Type ship coordinates and ship direction"
                    f" E.g.: A0 2 or A0 3\n0 - Up || 1 - Down || 2 - Left || 3 - Right\n"
                    f"Current ship: {ship}\nSize: {ship_size}\n").lower().split()
        direction, is_valid = check_valid_direction(grid, int(ship_position[1][0]), ship_size, 
                            (get_row_coordinates(ship_position), get_column_coordinates(ship_position)))
        if is_valid == True:
            return [direction, (get_row_coordinates(ship_position), get_column_coordinates(ship_position))]
        else:
            return handle_input_exception(grid)
    except:
        return handle_input_exception(grid)

# This function analyses grid availability in the desired direction without actually deploying units
def check_valid_direction(grid, direction, ship_size, ship_start):
    ship_position = []
    if direction == 0:
        if ship_start[0] - (ship_size - 1) >= 0:
            for x in range(ship_size):
                ship_position.append(grid[ship_start[0] - x][ship_start[1]])
            if ship_position.count(None) == ship_size and ship_position.count(0) == 0:
                return [direction, True]
    elif direction == 1:
        if ship_start[0] + ship_size <= len(grid):
            for x in range(ship_size):
                ship_position.append(grid[ship_start[0] + x][ship_start[1]])
            if ship_position.count(None) == ship_size and ship_position.count(0) == 0:
                return [direction, True]
    elif direction == 2:
        if ship_start[1] - (ship_size - 1) >= 0:
            for x in range(ship_size):
                ship_position.append(grid[ship_start[0]][ship_start[1] - x])
            if ship_position.count(None) == ship_size and ship_position.count(0) == 0:
                return [direction, True]
    elif direction == 3:
        if ship_start[1] + ship_size <= len(grid):
            for x in range(ship_size):
                ship_position.append(grid[ship_start[0]][ship_start[1] + x])
            if ship_position.count(None) == ship_size and ship_position.count(0) == 0:
                return [direction, True]
    return [direction, False]

# This function deploy units after confirming there are enough empty slots
def deploy_ship(grid, ship_size, ship_tag, ship_start, move_direction):
    if move_direction == 0:
        for i in range(ship_size):
            grid[ship_start[0] - i][ship_start[1]] = ship_tag
            create_collision_block(grid, ship_start[0] - i, ship_start[1])
    elif move_direction == 1:
        for i in range(ship_size):
            grid[ship_start[0] + i][ship_start[1]] = ship_tag
            create_collision_block(grid, ship_start[0] + i, ship_start[1])
    elif move_direction == 2:
        for i in range(ship_size):
            grid[ship_start[0]][ship_start[1] - i] = ship_tag
            create_collision_block(grid, ship_start[0], ship_start[1] - i)
    elif move_direction == 3:
        for i in range(ship_size):
            grid[ship_start[0]][ship_start[1] + i] = ship_tag
            create_collision_block(grid, ship_start[0], ship_start[1] + i)
    create_collision_block(grid, ship_start[0], ship_start[1])

# This function will create a collision block around each ship block when possible
def create_collision_block(grid, axis_Y, axis_X):
    if axis_Y + 1 < len(grid) and (grid[axis_Y + 1][axis_X] == None or grid[axis_Y + 1][axis_X] == 0):
        grid[axis_Y + 1][axis_X] = 0
    if axis_X + 1 < len(grid) and (grid[axis_Y][axis_X + 1] == None or grid[axis_Y][axis_X + 1] == 0):
        grid[axis_Y][axis_X + 1] = 0
    if axis_X - 1 >= 0 and (grid[axis_Y][axis_X - 1] == None or grid[axis_Y][axis_X - 1] == 0):
        grid[axis_Y][axis_X - 1] = 0
    if axis_Y - 1 >= 0 and (grid[axis_Y - 1][axis_X] == None or grid[axis_Y - 1][axis_X] == 0):
        grid[axis_Y - 1][axis_X] = 0

# A simple function to handle any input error while placing ships
def handle_input_exception(grid):
    print("Invalid values!")
    time.sleep(2)
    clear_console()
    print_board_open(grid, len(grid))
    return [0, ()]
