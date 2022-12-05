import boardModule
import placementModule
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
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "destroyer", player)
        placementModule.shipPlacement(grid, "battleship", player)


    elif difficulty == "normal":
        placementModule.shipPlacement(grid, "carrier", player)
        placementModule.shipPlacement(grid, "battleship", player)
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "destroyer", player)
        placementModule.shipPlacement(grid, "destroyer", player)


    elif difficulty == "hard":
        placementModule.shipPlacement(grid, "carrier", player)
        placementModule.shipPlacement(grid, "battleship", player)
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "destroyer", player)
        placementModule.shipPlacement(grid, "destroyer", player)
        placementModule.shipPlacement(grid, "destroyer", player)

def cpu_wins () -> bool:
    if cpu_ships == 0: return True
    return False

def player_wins () -> bool:
    if player_ships == 0: return True
    return False

if __name__ == "__main__":
    # grid_start("hard", False)
    # boardModule.clearConsole()
    # boardModule.print_board_open(grid_cpu, grid_size)

    # player & cpu lives
    player_ships = 0
    cpu_ships = 0

    print("Sea Battle - Matheus Alexandre & Symon Bezerra")
    diff_valid = False
    game_difficulty = 0
    while not diff_valid:    
        try:
            diff = int(input("Choose the game's difficulty:\n1 - Easy (5x5) | 2 - Normal (10x10) | 3 - Hard (15x15)"))
            boardModule.clearConsole()
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
                boardModule.clearConsole()
                print("Enter a value between 1-3!\n")
        except ValueError:
            boardModule.clearConsole()
            print("Enter a numeric value!\n")
    
    # now to start the grids
    grid_start(grid_cpu, game_difficulty, True)
    grid_start(grid_player, game_difficulty, True)

    boardModule.clearConsole()

    # these values will be switched back and forth
    player_turn = True
    cpu_turn = False

    # game loop check
    game_on = True
    while game_on:

        # how to end the game
        # if player_ships == 0:
        #     boardModule.clearConsole()
        #     print("CPU wins! Better luck next time =(")
        #     print("\n\nYour board:")
        #     boardModule.print_board_open(grid_player, len(grid_cpu))
        #     print("\n\nCPU's board:")
        #     boardModule.print_board_open(grid_cpu, len(grid_cpu))
        #     game_on = False
        # if cpu_ships == 0:
        #     boardModule.clearConsole()
        #     print("You win, congratulations! You're the Sea Master!")
        #     print("\n\nYour board:")
        #     boardModule.print_board_open(grid_player, len(grid_cpu))
        #     print("\n\nCPU's board:")
        #     boardModule.print_board_open(grid_cpu, len(grid_cpu))
        #     game_on = False 
        
        
        if player_turn:
            if player_wins():
                boardModule.clearConsole()
                print("CPU wins! Better luck next time =(")
                print("\n\nYour board:")
                boardModule.print_board_open(grid_player, len(grid_cpu))
                print("\n\nCPU's board:")
                boardModule.print_board_open(grid_cpu, len(grid_cpu))
                game_on = False

            else:
                boardModule.clearConsole()
                player_shooting = True
                while player_shooting:
                    if player_ships == 0 or cpu_ships == 0: break

                    try:
                        boardModule.print_board_open(grid_cpu, len(grid_cpu)) # debug
                        player_shot = input("\nAim your shot at the opponent! e.g.: B2\n").lower()
                        player_aim = grid_cpu[placementModule.getRowCoordinates(player_shot)][placementModule.getColumnCoordinates(player_shot)]
                        if player_aim == None or player_aim == 0:
                            grid_cpu[placementModule.getRowCoordinates(player_shot)][placementModule.getColumnCoordinates(player_shot)] = "M"
                            boardModule.clearConsole()
                            print("Miss!\n")
                            sleep(1.5)
                            # player_turn, cpu_turn = False, True
                            # player_shooting = False
                        elif player_aim in ("R", "B", "C", "D"):
                            boardModule.clearConsole()
                            print(f"You've hit the enemy's {SHIPS[player_aim]}!\n")
                            cpu_ships -= 1
                            grid_cpu[placementModule.getRowCoordinates(player_shot)][placementModule.getColumnCoordinates(player_shot)] = "H"
                            sleep(1.5)
                        elif player_aim in ("M", "H"):
                            boardModule.clearConsole()
                            print("You've already shot here! Choose another coordinate!\n")
                    except (KeyError, IndexError):
                        boardModule.clearConsole()
                        print("Enter a valid coordinate!\n")
        
        if cpu_turn:
            break # placeholder