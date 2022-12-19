import boardModule
import placementModule
from random import randint, shuffle
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
    if player_ships == 0: return True
    return False

def player_wins () -> bool:
    if cpu_ships == 0: return True
    return False

# cpu random shot
def cpu_randomshot () -> list:
    return [randint(0, grid_size - 1), randint(0, grid_size - 1)]

# if the CPU hits a ship, this will say the direction it must go
# def cpu_smartshot_direction (lastshot: list, ship: str) -> int:
#     valid_shot = False
#     while not valid_shot:
#         direction = randint(0,3)
#         cpu_shot = placementModule.cpu_check_valid_direction(grid_player, direction, ship, lastshot)
#         if cpu_shot: valid_shot = True
    
#     return direction

def cpu_smartshot (lasthit: tuple, direction: int) -> tuple:
    try:
        if direction == 0:
            return (lasthit[0] - 1, lasthit[1])
        elif direction == 1:
            return (lasthit[0] + 1, lasthit[1])
        elif direction == 2:
            return (lasthit[0], lasthit[1] - 1)
        elif direction == 3:
            return (lasthit[0], lasthit[1] + 1)
    except IndexError:
        return (None, None)
    
if __name__ == "__main__":

    # player & cpu lives
    player_ships = 0
    cpu_ships = 0

    # CPU auto attempts (AI)
    cpu_lasthits = []
    smartshot_directions = []
    # cpu_direction = 0

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
    grid_start(grid_player, game_difficulty, True)

    boardModule.clear_console()

    # these values will be switched back and forth
    player_turn = True
    cpu_turn = False

    # game loop check
    game_on = True
    while game_on:
        
        if player_turn:
            player_winner = player_wins()
            if player_winner:
                boardModule.clear_console()
                print("You win, congratulations! You're the Sea Master!")
                print("\n\nYour board:")
                boardModule.print_board_open(grid_player, len(grid_cpu))
                print("\n\nCPU's board:")
                boardModule.print_board_open(grid_cpu, len(grid_cpu))
                game_on = False
                break

            else:
                boardModule.clear_console()
                player_shooting = True
                while player_shooting:
                    if player_ships == 0 or cpu_ships == 0: break

                    try:
                        boardModule.print_board_open(grid_cpu, len(grid_cpu)) # debug
                        sleep(1.5)
                        player_shot = input("\nAim your shot at the opponent! e.g.: B2\n").lower()
                        player_aim = grid_cpu[placementModule.get_row_shot_coordinates(player_shot)][placementModule.get_column_shot_coordinates(player_shot)]
                        if player_aim == None or player_aim == 0:
                            grid_cpu[placementModule.get_row_shot_coordinates(player_shot)][placementModule.get_column_shot_coordinates(player_shot)] = "M"
                            boardModule.clear_console()
                            print("Miss!\n")
                            boardModule.print_board_open(grid_cpu, len(grid_cpu))
                            sleep(1.5)
                            player_turn, cpu_turn = False, True
                            player_shooting = False
                        elif player_aim in ("R", "B", "C", "D"):
                            ship_id = placementModule.get_ship_id_by_tag(player_aim)
                            boardModule.clear_console()
                            print(f"You've hit the CPU's {ship_id}")
                            cpu_ships -= 1
                            grid_cpu[placementModule.get_row_shot_coordinates(player_shot)][placementModule.get_column_shot_coordinates(player_shot)] = "H"
                            placementModule.check_destroyed_ships(grid_cpu)
                        elif player_aim in ("M", "H"):
                            boardModule.clear_console()
                            print("You've already shot here! Choose another coordinate!\n")
                    except (KeyError, IndexError):
                        boardModule.clear_console()
                        print("Enter a valid coordinate!\n")
        
        if cpu_turn:
            cpu_winner = cpu_wins()
            if cpu_winner:
                boardModule.clear_console()
                print("CPU wins! Better luck next time =(")
                print("\n\nYour board:")
                boardModule.print_board_open(grid_player, len(grid_cpu))
                print("\n\nCPU's board:")
                boardModule.print_board_open(grid_cpu, len(grid_cpu))
                game_on = False 
                break
            else:
                boardModule.clear_console()
                print("CPU is going to make a shot...\n")
                boardModule.print_board_open(grid_player, len(grid_player))
                sleep(1.5)

                if len(cpu_lasthits) == 0:
                    cpu_attempt = False
                else:
                    cpu_attempt = placementModule.cpu_unfinished_business(grid_player)
                if not cpu_attempt:
                    cpu_aim = cpu_randomshot()
                else:
                    valid_shot = False
                    while not valid_shot:
                        cpu_aim = cpu_smartshot(cpu_lasthits[len(cpu_lasthits) - 1], smartshot_directions[len(smartshot_directions) - 1])
                        if cpu_aim != (None, None):
                            valid_shot = True
                        else:
                            smartshot_directions.pop()
                try:
                    cpu_shot = grid_player[cpu_aim[0]][cpu_aim[1]]
                except IndexError:
                    cpu_attempt = False
                    cpu_aim = cpu_randomshot()

                if cpu_shot in ("R", "B", "D", "C"):
                    if not cpu_attempt:
                        smartshot_directions = [0,1,2,3]
                        shuffle(smartshot_directions)
                    ship_id = placementModule.get_ship_id_by_tag(cpu_shot)
                    cpu_lasthits.append(cpu_aim)
                    player_ships -= 1
                    grid_player[cpu_aim[0]][cpu_aim[1]] = "H"
                    boardModule.clear_console()
                    print(f"CPU has hit your {ship_id}!\n")
                    boardModule.print_board_open(grid_player, len(grid_player))
                    sleep(1.5)
                elif cpu_shot in ("M", "H"):
                    if len(smartshot_directions) > 0:
                        smartshot_directions.pop()
                    elif len(smartshot_directions) == 0:
                        cpu_attempt == False
                elif cpu_shot in (None, 0):
                    auto_attempts = 0
                    grid_player[cpu_aim[0]][cpu_aim[1]] = "M"
                    boardModule.clear_console()
                    print(f"CPU has missed!\n")
                    boardModule.print_board_open(grid_player, len(grid_player))
                    sleep(1.5)
                    player_turn, cpu_turn = True, False