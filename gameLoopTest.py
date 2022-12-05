import boardModule
import placementModule
from random import randint
from time import sleep

# global variables
grid_cpu = []
grid_player = []
grid_size = 0

DIFFICULTY = {"easy": 5, "normal": 10, "hard": 15}
SHIPS = {"R": "Carrier", "B": "Battleship", "C": "Cruiser", "D": "Destroyer"}
# grid initializer
def grid_start (grid: list, difficulty: str, player: bool):
    grid_size = DIFFICULTY[difficulty]
    
    # initializing grid
    boardModule.start_board(grid, grid_size)
    boardModule.print_board(grid, grid_size)       
    
    if difficulty == "easy":
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "battleship", player)


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
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "cruiser", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)
        placementModule.ship_placement(grid, "destroyer", player)

def cpu_wins () -> bool:
    if cpu_ships == 0: return True
    return False

def player_wins () -> bool:
    if player_ships == 0: return True
    return False

def cpu_autoshot () -> tuple:
    return (randint(0, grid_size - 1), randint(0, grid_size - 1), randint(0,3))
    # row, column, direction

if __name__ == "__main__":
    # grid_start("hard", False)
    # boardModule.clear_console()
    # boardModule.print_board_open(grid_cpu, grid_size)

    # player & cpu lives
    player_ships = 0
    cpu_ships = 0

    # CPU auto attempts (AI)
    auto_attemps = 0
    cpu_lastshot = (0,0,0)

    print("Sea Battle - Matheus Alexandre & Symon Bezerra")
    diff_valid = False
    game_difficulty = 0
    while not diff_valid:    
        try:
            diff = int(input("Choose the game's difficulty:\n1 - Easy (5x5) | 2 - Normal (10x10) | 3 - Hard (15x15)"))
            boardModule.clear_console()
            if diff == 1: 
                game_difficulty = "easy"
                player_ships, cpu_ships = 10, 10
                diff_valid = True
            elif diff == 2: 
                game_difficulty = "normal"
                player_ships, cpu_ships = 19, 19
                diff_valid = True
            elif diff == 3: 
                game_difficulty = "hard"
                player_ships, cpu_ships = 28, 28
                diff_valid = True
            else:
                boardModule.clear_console()
                print("Enter a value between 1-3!\n")
        except ValueError:
            boardModule.clear_console()
            print("Enter a numeric value!\n")
    
    # now to start the grids
    grid_start(grid_cpu, game_difficulty, True)
    grid_start(grid_player, game_difficulty, True)

    boardModule.clear_console()

    # these values will be switched back and forth
    player_turn = True
    cpu_turn = False

    # game loop check
    game_on = True
    while game_on:
        
        if player_turn:
            if player_wins():
                boardModule.clear_console()
                print("CPU wins! Better luck next time =(")
                print("\n\nYour board:")
                boardModule.print_board_open(grid_player, len(grid_cpu))
                print("\n\nCPU's board:")
                boardModule.print_board_open(grid_cpu, len(grid_cpu))
                game_on = False

            else:
                boardModule.clear_console()
                player_shooting = True
                while player_shooting:
                    if player_ships == 0 or cpu_ships == 0: break

                    try:
                        boardModule.print_board(grid_cpu, len(grid_cpu)) # debug
                        player_shot = input("\nAim your shot at the opponent! e.g.: B2\n").lower()
                        player_aim = grid_cpu[placementModule.get_row_coordinates(player_shot)][placementModule.get_column_coordinates(player_shot)]
                        if player_aim == None or player_aim == 0:
                            grid_cpu[placementModule.get_row_coordinates(player_shot)][placementModule.get_column_coordinates(player_shot)] = "M"
                            boardModule.clear_console()
                            print("Miss!\n")
                            sleep(1.5)
                            player_turn, cpu_turn = False, True
                            player_shooting = False
                        elif player_aim in ("R", "B", "C", "D"):
                            boardModule.clear_console()
                            print(f"You've hit the enemy's {SHIPS[player_aim]}!\n")
                            cpu_ships -= 1
                            grid_cpu[placementModule.get_row_coordinates(player_shot)][placementModule.getColumnCoordinates(player_shot)] = "H"
                            sleep(1.5)
                        elif player_aim in ("M", "H"):
                            boardModule.clear_console()
                            print("You've already shot here! Choose another coordinate!\n")
                    except (KeyError, IndexError):
                        boardModule.clear_console()
                        print("Enter a valid coordinate!\n")
        
        if cpu_turn:
            if cpu_wins():
                boardModule.clear_console()
                print("You win, congratulations! You're the Sea Master!")
                print("\n\nYour board:")
                boardModule.print_board_open(grid_player, len(grid_cpu))
                print("\n\nCPU's board:")
                boardModule.print_board_open(grid_cpu, len(grid_cpu))
                game_on = False 

            else:
                boardModule.clear_console()
                print("CPU is going to make a shot...\n")
                boardModule.print_board_open(grid_player, len(grid_player))
                # random coord

                if auto_attemps == 0:
                    cpu_attempt = cpu_autoshot()
                    cpu_aim = grid_player[cpu_autoshot[0]][cpu_autoshot[1]]
                else:
                    auto_attemps -= 1
                    if cpu_lastshot(2) == 0:
                        cpu_aim = grid_player[cpu_autoshot[0] - 1][cpu_autoshot[1]]
                    elif cpu_lastshot(2) == 1:
                        grid_player[cpu_autoshot[0] + 1][cpu_autoshot[1]]
                    elif cpu_lastshot(2) == 2:
                        grid_player[cpu_autoshot[0]][cpu_autoshot[1] - 1]
                    elif cpu_lastshot(3) == 3:
                        grid_player[cpu_autoshot[0]][cpu_autoshot[1] + 1]

                if cpu_aim in ("R", "B", "D", "C"):
                    cpu_lastshot = cpu_attempt
                    boardModule.clear_console()
                    print(f"CPU has hit your {SHIPS[cpu_aim]}!\n")
                    sleep(1.5)
                    boardModule.print_board_open(grid_player, len(grid_player))
                    ship_id = placementModule.get_ship_id(SHIPS[cpu_aim].lower())[0]
                    auto_attemps = ship_id[0] - 1
                elif cpu_aim in ("M", "H"):
                    auto_attemps = 0
                elif cpu_aim in (None, 0):
                    boardModule.clear_console()
                    print(f"CPU has missed!\n")
                    sleep(1.5)
                    boardModule.print_board_open(grid_player, len(grid_player))
                    player_turn, cpu_turn = True, False