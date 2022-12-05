import boardModule
import placementModule
from time import sleep

# global variables
grid_cpu = []
grid_player = []
grid_size = 0
DIFFICULTY = {"easy": 5, "normal": 10, "hard": 15}
TOP_COORDINATES = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O")
# CPU grid
def grid_start (grid: list, difficulty: str, player: bool):
    grid_size = DIFFICULTY[difficulty]
    
    # initializing grid
    boardModule.start_board(grid, grid_size)
    boardModule.print_board(grid, grid_size)       
    
    if difficulty == "easy":
        placementModule.shipPlacement(grid, "battleship", player)
        placementModule.shipPlacement(grid, "cruiser", player)
        placementModule.shipPlacement(grid, "destroyer", player)
        placementModule.shipPlacement(grid, "destroyer", player)


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
            diff = int(input("Choose the game's difficulty:\n1 - Fácil (5x5) | 2 - Médio (10x10) | 3 - Difícil (15x15)"))
            boardModule.clearConsole()
            if diff == 1: 
                game_difficulty = "easy"
                player_ships, cpu_ships = 11, 11
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
        if player_ships == 0:
            boardModule.clearConsole()
            print("CPU wins! Better luck next time =(")
            print("\n\nYour board:")
            boardModule.print_board_open(grid_player, len(grid_cpu))
            print("\n\nCPU's board:")
            boardModule.print_board_open(grid_cpu, len(grid_cpu))
            game_on = False
        if cpu_ships == 0:
            boardModule.clearConsole()
            print("You win, congratulations! You're the Sea Master!")
            print("\n\nYour board:")
            boardModule.print_board_open(grid_player, len(grid_cpu))
            print("\n\nCPU's board:")
            boardModule.print_board_open(grid_cpu, len(grid_cpu))
            game_on = False 
        
        
        if player_turn:
            boardModule.clearConsole()
            player_shooting = True
            while player_shooting:
                if player_ships == 0 or cpu_ships == 0: break

                try:
                    boardModule.print_board_open(grid_cpu, len(grid_cpu)) # debug
                    player_shot = input("\nAim your shot at the opponent! e.g.: B 2 (use a space here)").split()
                    player_aim = grid_cpu[int(player_shot[1])][TOP_COORDINATES.index(player_shot[0])]
                    if player_aim == None or player_aim == 0:
                        grid_cpu[int(player_shot[1])][TOP_COORDINATES.index(player_shot[0])] = "M"
                        boardModule.clearConsole()
                        print("Miss\n")
                        sleep(1.5)
                        # player_turn, cpu_turn = False, True
                        # player_shooting = False
                    elif player_aim in ("R", "B", "C", "D"):
                        boardModule.clearConsole()
                        print("Hit!\n")
                        cpu_ships -= 1
                        grid_cpu[int(player_shot[1])][TOP_COORDINATES.index(player_shot[0])] = "H"
                        sleep(1.5)
                except KeyError or IndexError:
                    boardModule.clearConsole()
                    print("Enter a valid coordinate!\n")
        
        if cpu_turn:
            break # placeholder