import time
import placementModule
from random import randint, shuffle
from boardModule import print_board, print_board_open
from boardModule import clear_console

# Global ships memory
ships_memory = placementModule.ships_memory
cpu_last_hit_memory = []

# Getting random coordinates for CPU shot
def cpu_random_coordinates(grid: list) -> tuple:
    cpu_random_coordinates = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
    return cpu_random_coordinates

def cpu_unfinished_business(grid: list, ships_memory: list) -> tuple:
    for ship in ships_memory:
        if "player" not in ship:
            pass
        else:
            ship_tags = []
            ship_coordinates = []
            for cell in range(len(ship)):
                if cell > 0:
                    axis_Y = ship[cell][0]
                    axis_X = ship[cell][1]
                    ship_tags.append(grid[axis_Y][axis_X])
                    ship_coordinates.append(ship[cell])
            if ship_tags.count("H") < len(ship) - 1 and ship_tags.count("H") > 0:
                for coordinates in range(len(ship_tags)):
                    if coordinates < len(ship_tags) - 1:
                        if ship_tags[coordinates] == "H" and ship_tags[coordinates + 1] != "H":
                            return ship_coordinates[coordinates]
                    if coordinates > 0:
                        if ship_tags[coordinates] == "H" and ship_tags[coordinates - 1] != "H":
                            return ship_coordinates[coordinates]
                    if coordinates == len(ship_tags) - 1 and ship_tags[coordinates] != "H":
                        return ship_coordinates[coordinates]
    cpu_last_hit_memory.clear()
    return None

def game_finish(player_wins: bool, cpu_wins: bool, grid_cpu: list, grid_player: list):
    if player_wins:
        clear_console()
        print("You win, congratulations! You're the Sea Master!")
        print("\n\nYour board:")
        print_board_open(grid_player, len(grid_player))
        print("\n\nCPU's board:")
        print_board_open(grid_cpu, len(grid_cpu))
    elif cpu_wins:
        clear_console()
        print("CPU wins! Good luck next time.")
        print("\n\nYour board:")
        print_board_open(grid_player, len(grid))
        print("\n\nCPU's board:")
        print_board_open(grid_cpu, len(grid))
    
def player_shot(grid: list) -> tuple:
    print_board(grid, len(grid))
    valid_input = False
    while not valid_input:
        try:
            shot_coordinates = input("Aim your shot at your oponent! e.g. B2:\n")
        except (KeyError, ValueError):
            print("\nInvalid Coordinates!")
            time.sleep(2)
            print_board(grid, len(grid))
        try:
            if (placementModule.get_row_shot_coordinates(shot_coordinates) < len(grid) or placementModule.get_row_shot_coordinates(shot_coordinates) >= 0) \
            and (placementModule.get_column_shot_coordinates(shot_coordinates) < len(grid) or placementModule.get_column_shot_coordinates(shot_coordinates) >= 0):
                valid_input = True
        except TypeError:
            continue
    return (placementModule.get_row_shot_coordinates(shot_coordinates), placementModule.get_column_shot_coordinates(shot_coordinates))



def smart_shot(grid: list, cpu_shot_coordinates: tuple):
    axis_Y = cpu_shot_coordinates[0]
    axis_X = cpu_shot_coordinates[1]
    if axis_Y + 1 < len(grid):
        cpu_last_hit_memory.append(((axis_Y + 1, axis_X), 1))
    if axis_Y - 1 >= 0:
        cpu_last_hit_memory.append(((axis_Y - 1, axis_X), 0))
    if axis_X + 1 < len(grid):
        cpu_last_hit_memory.append(((axis_Y, axis_X + 1), 3))
    if axis_X - 1 >= 0:
        cpu_last_hit_memory.append(((axis_Y, axis_X - 1), 2))
    shuffle(cpu_last_hit_memory)
    for cell in range(len(cpu_last_hit_memory)):
            axis_Y = cpu_last_hit_memory[cell][0][0]
            axis_X = cpu_last_hit_memory[cell][0][1]
            direction = cpu_last_hit_memory[cell][1]
            if grid[axis_Y][axis_X] not in ["H", "M"]:
                return [(axis_Y, axis_X), direction]
            else:
                cpu_last_hit_memory.pop(cell)

def smart_chainer(grid: list, coordinates: tuple, direction: int):
    axis_Y = coordinates[0]
    axis_X = coordinates[1]
    if direction == 0:
        if axis_Y -1 >= 0:
            return (axis_Y - 1, axis_X)
        else:
            direction = 1
    if direction == 1:
        if axis_Y + 1 < len(grid):
            return (axis_Y + 1, axis_X)
        else:
            direction = 2
    if direction == 2:
        if axis_X - 1 >= 0:
            return (axis_Y, axis_X - 1)
        else:
            direction = 3
    if direction == 3:
        if axis_X + 1 < len(grid):
            return (axis_Y, axis_X + 1)
        else:
            return cpu_random_coordinates(grid)


def player_turn(grid: list) -> bool:
    cpu_ships = 0
    end_turn = False
    if not check_cpu_ships_left():
        end_turn = True
        return (end_turn, 0)
    while not end_turn:
        valid_shot = False
        while not valid_shot:
            clear_console()
            player_shot_coordinates = player_shot(grid)
            if player_shot_coordinates[0] < len(grid) and player_shot_coordinates[1] < len(grid):
                player_aim = grid[player_shot_coordinates[0]][player_shot_coordinates[1]]
                valid_shot = True
        if player_aim in ["R", "B", "C", "D"]:
            clear_console()
            cpu_ships += 1
            ship_id = placementModule.get_ship_id_by_tag(player_aim)
            print(f"You've hit CPU's {ship_id}\n\n")
            grid[player_shot_coordinates[0]][player_shot_coordinates[1]] = "H"
            print_board(grid, len(grid))
            time.sleep(2)
            placementModule.check_destroyed_ships(grid, False)
        elif player_aim == "M":
            print("You already shot here! Choose another coordinate!\n\n")
            time.sleep(2)
        elif player_aim in [0, None]:
            clear_console()
            print(f"Miss!\n\n")
            grid[player_shot_coordinates[0]][player_shot_coordinates[1]] = "M"
            print_board(grid, len(grid))
            end_turn = True
            time.sleep(2)
    clear_console()
    return (end_turn, cpu_ships)

def cpu_turn(grid: list, end_turn: bool) -> list:
    player_ships = 0
    direction = -1
    while end_turn:
        valid_shot = False
        ships_hit = cpu_unfinished_business(grid, ships_memory)
        while not valid_shot:
            clear_console()
            if ships_hit != None and direction >= 0:
                cpu_shot_coordinates = smart_chainer(grid, cpu_shot_coordinates, direction)
            if ships_hit != None and direction < 0:
                cpu_shot_coordinates, direction = smart_shot(grid, ships_hit)
                cpu_aim = grid[cpu_shot_coordinates[0]][cpu_shot_coordinates[1]]
            else:
                cpu_shot_coordinates = cpu_random_coordinates(grid)
                cpu_aim = grid[cpu_shot_coordinates[0]][cpu_shot_coordinates[1]]
            if cpu_aim not in ["H", "M"]:
                valid_shot = True
                print("CPU is aiming it's shot...")
                print_board_open(grid, len(grid))
                time.sleep(2)
        if cpu_aim in ["R", "B", "C", "D"]:
            clear_console()
            player_ships += 1
            ship_id = placementModule.get_ship_id_by_tag(cpu_aim)
            if direction >= 0:
                cpu_last_hit_memory.clear()
            print(f"CPU hit your {ship_id}")
            grid[cpu_shot_coordinates[0]][cpu_shot_coordinates[1]] = "H"
            print_board_open(grid, len(grid))
            time.sleep(2)
            placementModule.check_destroyed_ships(grid, True)
        elif cpu_aim in [0, None]:
            clear_console()
            print(f"Miss!")
            direction = -1
            grid[cpu_shot_coordinates[0]][cpu_shot_coordinates[1]] = "M"
            print_board_open(grid, len(grid))
            time.sleep(2)
            end_turn = False
    clear_console()
    return (end_turn, player_ships)

def check_cpu_ships_left():
    acm = 0
    for ship in ships_memory:
        if "cpu" in ship:
            acm += 1
        else:
            pass
        if acm > 0:
            return True
    else:
        return False