import time
from random import randint, shuffle
from boardModule import print_board, print_board_open
from boardModule import clear_console

# Global Variable to hold ships coordinates
ships_memory = []

# direction variable is used several times in this file. 
## direction == 0: up, 1: down, 2: left, 3: right

# Main module for ship placement. 
# Auto should be True for autoplacement and False for manual input.
def ship_placement(grid: list, ship: str, auto: bool):
    grid = grid
    if auto:
        direction, ship_start = auto_ship_placement(grid, ship, auto)
    else:
        direction, ship_start = do_manual_input(grid, ship)
        while len(ship_start) < 1:
            direction, ship_start = do_manual_input(grid, ship)
    deploy_ship(grid, ship, ship_start, direction)
    clear_console()
    if auto: 
        print("\n\nCPU is placing its ships...")
        print_board(grid, len(grid))
    else:
        print_board_open(grid, len(grid))
    time.sleep(1)

# This function is used for autoplacement.
def auto_ship_placement(grid: list, ship_size: int, auto: bool) -> list:
    direction = randint(0, 3)
    ship_start = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
    move_direction, is_valid = check_valid_placement_direction(grid, direction, ship_size, ship_start, auto)
    while is_valid == False:
        direction = randint(0, 3)
        ship_start = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
        move_direction, is_valid = check_valid_placement_direction(grid, direction, ship_size, ship_start, auto)
    return [move_direction, ship_start]

# \/\/\/ Simple functions to identify ships \/\/\/

def get_ship_id_by_size(ship_size: int) -> str:
    if ship_size == 5:
        return "Carrier"
    elif ship_size == 4:
        return "Battleship"
    elif ship_size == 3:
        return "Cruiser"
    elif ship_size == 2:
        return "Destroyer"
    else:
        return ""

def get_ship_tag_by_id(ship: str) -> str:
    if ship == "carrier":
        return "R"
    elif ship == "battleship":
        return "B"
    elif ship == "cruiser":
        return "C"
    elif ship == "destroyer":
        return "D"

def get_ship_id_by_tag(ship_tag: str) -> str:
    if ship_tag == "R":
        return "Carrier"
    elif ship_tag == "B":
        return "Battleship"
    elif ship_tag == "C":
        return "Cruiser"
    elif ship_tag == "D":
        return "Destroyer"

def get_ship_size(ship_name_or_tag: str) -> int:
    if ship_name_or_tag == "R" or ship_name_or_tag == "carrier":
        return 5
    elif ship_name_or_tag == "B" or ship_name_or_tag == "battleship":
        return 4
    elif ship_name_or_tag == "C" or ship_name_or_tag == "cruiser":
        return 3
    elif ship_name_or_tag == "D" or ship_name_or_tag == "destroyer":
        return 2
    else:
        return 0
# /\/\/\ Simple functions to identify ships /\/\/\

# Simple functions to get a specific coordinate in user input
# Both arguments must be STRING type. 
# e.g.: if user inputs D4 as coordinate, you may call get_column_coordinates(input) 
# to reach column D and get_row_coordinates(input) to reach row 4
def get_column_coordinates(player_input: str) -> int:
    try:
        if len(player_input[0]) > 1 and len(player_input[0]) < 4:
            coordinate = player_input[0][0].lower()
            return ord(coordinate) - ord("a")
    except ValueError:
        return ord("z")
def get_row_coordinates(player_input: str) -> int:
    try:
        if len(player_input[0]) < 3:
            return int(player_input[0][1])
        elif len(player_input[0]) >= 3:
            return (int(player_input[0][1]) * 10) + int(player_input[0][2])
    except ValueError:
        return 16


# Get column/rows and get shot column/rows works almost the same, 
# but the above code should be used for placement, 
# while code below is for use during gameloop only.
def get_column_shot_coordinates(player_input: str) -> int:
    try:
        if len(player_input) > 1 and len(player_input) < 4:
            coordinate = player_input[0].lower()
            return ord(coordinate) - ord("a")
    except ValueError:
        return ord("z")

def get_row_shot_coordinates(player_input: str) -> int:
    try:
        if len(player_input) < 3:
            return int(player_input[1])
        elif len(player_input) >= 3:
            return (int(player_input[1]) * 10) + int(player_input[2])
    except ValueError:
        return 16

# A specific function to receive player input during placement
def do_manual_input(grid: list, ship: str) -> list:
    is_valid = False
    try:
        ship_position = input("Type ship coordinates and ship direction"
                    f" E.g.: A0 2 or A0 3\n0 - Up || 1 - Down || 2 - Left || 3 - Right\n"
                    f"Current ship: {ship}\nSize: {get_ship_size(ship)}\n").split()
        direction, is_valid = check_valid_placement_direction(grid, int(ship_position[1][0]), ship, 
                            (get_row_coordinates(ship_position), get_column_coordinates(ship_position)), False)
        if is_valid == True:
            return [direction, (get_row_coordinates(ship_position), get_column_coordinates(ship_position))]
        else:
            return handle_input_exception(grid)
    except:
        return handle_input_exception(grid)

# This function analyses grid availability in the desired direction without actually deploying units
def check_valid_placement_direction(grid: list, direction: int, ship: str, ship_start: list, auto: bool) -> list:
    ship_position = []
    ships_temporary_coordinates = []
    axis_Y = ship_start[0]
    axis_X = ship_start[1]
    if auto:
        ships_temporary_coordinates.append("cpu")
    else:
        ships_temporary_coordinates.append("player")
    if direction == 0:
        if axis_Y - (get_ship_size(ship) - 1) >= 0:
            for x in range(get_ship_size(ship)):
                ship_position.append(grid[axis_Y - x][axis_X])
                ships_temporary_coordinates.append((axis_Y - x, axis_X))
            if ship_position.count(None) == (get_ship_size(ship)):
                ships_memory.append(ships_temporary_coordinates)
                return [direction, True]

    elif direction == 1:
        if axis_Y + (get_ship_size(ship)) <= len(grid):
            for x in range(get_ship_size(ship)):
                ship_position.append(grid[axis_Y + x][axis_X])
                ships_temporary_coordinates.append((axis_Y + x, axis_X))
            if ship_position.count(None) == (get_ship_size(ship)):
                ships_memory.append(ships_temporary_coordinates)
                return [direction, True]

    elif direction == 2:
        if axis_X - (get_ship_size(ship) - 1) >= 0:
            for x in range(get_ship_size(ship)):
                ship_position.append(grid[axis_Y][axis_X - x])
                ships_temporary_coordinates.append((axis_Y, axis_X - x))
            if ship_position.count(None) == (get_ship_size(ship)):
                ships_memory.append(ships_temporary_coordinates)
                return [direction, True]

    elif direction == 3:
        if axis_X + (get_ship_size(ship)) <= len(grid):
            for x in range(get_ship_size(ship)):
                ship_position.append(grid[axis_Y][axis_X + x])
                ships_temporary_coordinates.append((axis_Y, axis_X + x))
            if ship_position.count(None) == (get_ship_size(ship)):
                ships_memory.append(ships_temporary_coordinates)
                return [direction, True]
    return [direction, False]



# This function deploy units after confirming there are enough empty slots
def deploy_ship(grid: list, ship: str, ship_start: list, move_direction: int):
    axis_Y = ship_start[0]
    axis_X = ship_start[1]
    if move_direction == 0:

        for i in range(get_ship_size(ship)):
            grid[axis_Y - i][axis_X] = get_ship_tag_by_id(ship)
            create_collision_block(grid, axis_Y - i, axis_X)

    elif move_direction == 1:

        for i in range(get_ship_size(ship)):
            grid[axis_Y + i][axis_X] = get_ship_tag_by_id(ship)
            create_collision_block(grid, axis_Y + i, axis_X)

    elif move_direction == 2:
        for i in range(get_ship_size(ship)):

            grid[axis_Y][axis_X - i] = get_ship_tag_by_id(ship)
            create_collision_block(grid, axis_Y, axis_X - i)

    elif move_direction == 3:

        for i in range(get_ship_size(ship)):
            grid[axis_Y][axis_X + i] = get_ship_tag_by_id(ship)
            create_collision_block(grid, axis_Y, axis_X + i)

    create_collision_block(grid, axis_Y, axis_X)

# This function will create a collision block around each ship block when possible
def create_collision_block(grid: list, axis_Y: int, axis_X: int):
    if axis_Y + 1 < len(grid) and (grid[axis_Y + 1][axis_X] == None or grid[axis_Y + 1][axis_X] == 0):
        grid[axis_Y + 1][axis_X] = 0
    if axis_X + 1 < len(grid) and (grid[axis_Y][axis_X + 1] == None or grid[axis_Y][axis_X + 1] == 0):
        grid[axis_Y][axis_X + 1] = 0
    if axis_X - 1 >= 0 and (grid[axis_Y][axis_X - 1] == None or grid[axis_Y][axis_X - 1] == 0):
        grid[axis_Y][axis_X - 1] = 0
    if axis_Y - 1 >= 0 and (grid[axis_Y - 1][axis_X] == None or grid[axis_Y - 1][axis_X] == 0):
        grid[axis_Y - 1][axis_X] = 0

def check_destroyed_ships(grid: list, open: bool) -> None:
    for ship in ships_memory:
        ship_tags = []
        for cell in range(len(ship)):
            if cell > 0:
                axis_Y = ship[cell][0]
                axis_X = ship[cell][1]
                ship_tags.append(grid[axis_Y][axis_X])
        if ship_tags.count("H") == len(ship) - 1:
            clear_console()
            if open:
                print_board_open(grid, len(grid))
            else:
                print_board(grid, len(grid))
            time.sleep(1)
            show_collision_blocks(grid, ship, open)
            remove_ship_from_memory(ships_memory, ships_memory.index(ship))
            break

def show_collision_blocks(grid: list, ship: list, open: bool) -> None:
    for cell in range(len(ship)):
        if cell > 0:
            axis_Y = ship[cell][0]
            axis_X = ship[cell][1]
            if axis_Y + 1 < len(grid) and grid[axis_Y + 1][axis_X] == 0:
                grid[axis_Y + 1][axis_X] = "M"
                update_collision_blocks(grid, open)
            if axis_Y - 1 >= 0 and grid[axis_Y - 1][axis_X] == 0:
                grid[axis_Y - 1][axis_X] = "M"
                update_collision_blocks(grid, open)
            if axis_X + 1 < len(grid) and grid[axis_Y][axis_X + 1] == 0:
                grid[axis_Y][axis_X + 1] = "M"
                update_collision_blocks(grid, open)
            if axis_X - 1 >= 0 and grid[axis_Y][axis_X - 1] == 0:
                grid[axis_Y][axis_X - 1] = "M"
                update_collision_blocks(grid, open)
    time.sleep(1)

def update_collision_blocks(grid: list, open: bool):
    time.sleep(0.5)
    clear_console()
    if open:
        print_board_open(grid, len(grid))
    else:
        print_board(grid, len(grid))
        
def remove_ship_from_memory(ships_memory: list, number_index: int) -> None:
    ships_memory.pop(number_index)

# A simple function to handle any input error while placing ships
def handle_input_exception(grid: list) -> list:
    print("Invalid values!")
    time.sleep(2)
    clear_console()
    print_board_open(grid, len(grid))
    return [0, ()]