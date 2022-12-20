import boardModule
import placementModule
import gameModule
from random import randint
from time import sleep

# global variables
grid_cpu = []
grid_player = []
grid_size = 0

DIFFICULTY = {"easy": 5, "normal": 10, "hard": 15}
SHIPS = {"R": "Carrier", "B": "Battleship", "C": "Cruiser", "D": "Destroyer"}
SHIP_SIZES = {"R": 5, "B": 4, "C": 3, "D": 2}
# grid initializer
def grid_start (grid: list, difficulty: str, player: bool):

    # initializing grid
    boardModule.start_board(grid, grid_size)
    boardModule.print_board(grid, grid_size)       

    if difficulty == "easy":
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)

    elif difficulty == "normal":
        placementModule.ship_placement(grid, "carrier", player)
        placementModule.ship_placement(grid, "battleship", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)


    elif difficulty == "hard":
        placementModule.ship_placement(grid, "carrier", player)
        placementModule.ship_placement(grid, "battleship", player)
        placementModule.ship_placement(grid, "battleship", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)


# game loop conditions
def cpu_wins () -> bool:
    if player_ships == 0:
        game_on = False
        gameModule.game_finish(False, True) 
        return True
    return False

def player_wins () -> bool:
    if cpu_ships == 0: 
        game_on = False
        gameModule.game_finish(True, False)
        return True
    return False

if __name__ == "__main__":

    # player & cpu lives
    player_ships = 0
    cpu_ships = 0

    print("Sea Battle - Matheus Alexandre & Symon Bezerra")
    diff_valid = False
    game_difficulty = 0
    while not diff_valid:    
        try:
            diff = int(input("Choose the game's difficulty:\n1 - Easy (5x5) | 2 - Normal (10x10) | 3 - Hard (15x15)\n"))
            boardModule.clear_console()
            if diff == 1: 
                game_difficulty = "easy"
                player_ships, cpu_ships = 9, 9
                diff_valid = True
            elif diff == 2: 
                game_difficulty = "normal"
                player_ships, cpu_ships = 19, 19
                diff_valid = True
            elif diff == 3: 
                game_difficulty = "hard"
                player_ships, cpu_ships = 24, 24
                diff_valid = True
            else:
                boardModule.clear_console()
                print("Enter a value between 1-3!\n")
            grid_size = DIFFICULTY[game_difficulty]
        except ValueError:
            boardModule.clear_console()
            print("Enter a numeric value!\n")

    # now to start the grids
    grid_start(grid_cpu, game_difficulty, True)
    boardModule.clear_console()
    grid_start(grid_player, game_difficulty, False)
    boardModule.clear_console()

    # Adding ships coordinates to main memory
    ships_memory = placementModule.ships_memory

    # game loop check
    game_on = True
    while game_on:
        if cpu_wins() or player_wins() == True:
            break
        else:
            player_shot_coordinates = gameModule.playerShot(grid_cpu)
            player_aim = grid_cpu[player_shot_coordinates[0]][player_shot_coordinates[1]]
            if player_aim in SHIPS:
                ship_id = placementModule.get_ship_id_by_tag(player_aim)
                cpu_ships -= 1
                print(f"You've hit CPU's {ship_id}")
            placementModule.check_destroyed_ships(grid_cpu, False)
            time.sleep(1)
