import time
from random import randint, shuffle
from boardModule import print_board, print_board_open
from boardModule import clear_console

# Getting random coordinates for CPU shot
def cpu_random_coordinates(grid: list) -> tuple:
    cpu_random_coordinates = (randint(0, len(grid) - 1), randint(0, len(grid) - 1))
    return cpu_random_coordinates

def cpu_unfinished_business(grid: list, ships_memory: list, open: bool) -> tuple:
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
                        else:
                            pass
                    else:
                        if ship_tags[coordinates] != "H":
                            return ship_coordinates[coordinates]
                        else:
                            placementModule.check_destroyed_ships(grid, open)
                            return None
            elif ship_tags.count("H") == len(ship) - 1:
                placementModule.check_destroyed_ships(grid, open)
                return None
    return None

def game_finish(player_wins: bool, cpu_wins: bool):
    if player_wins:
        boardModule.clear_console()
        print("You win, congratulations! You're the Sea Master!")
        print("\n\nYour board:")
        boardModule.print_board_open(grid_player, len(grid_cpu))
        print("\n\nCPU's board:")
        boardModule.print_board_open(grid_cpu, len(grid_cpu))
    elif cpu_wins:
        boardModule.clear_console()
        print("CPU wins! Good luck next time.")
        print("\n\nYour board:")
        boardModule.print_board_open(grid_player, len(grid_cpu))
        print("\n\nCPU's board:")
        boardModule.print_board_open(grid_cpu, len(grid_cpu))
    
def player_shot(grid: list) -> tuple:
    shot_coordinates = input("Aim your shot at your oponent! e.g. B2:/n")
    print_board(grid, len(grid))
    return (placementModule.get_row_shot_coordinates(shot_coordinates), placementModule.get_column_shot_coordinates(shot_coordinates))